from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, QuizSession, QuizHistory
from django.db.models import Count
import random
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Home Page
def home(request):
    subjects = [
        {'name': 'Django', 'image': 'images/django.png'},
        {'name': 'Science', 'image': 'images/science.png'},
        {'name': 'GK', 'image': 'images/GK.png'},
        {'name': 'Countries', 'image': 'images/countries.png'},
        {'name': 'History', 'image': 'images/history.png'}
    ]
    return render(request, 'home.html', {'subjects': subjects})

@login_required(login_url='/login/')
def start_quiz(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')  
        if not subject:
            return redirect('home')  

        if 'quiz_session_id' in request.session:
            previous_session = QuizSession.objects.get(id=request.session['quiz_session_id'])
            previous_session.end_time = timezone.now()  # Mark the session as ended
            previous_session.save()

        session = QuizSession.objects.create(user=request.user, subject=subject)

        request.session['quiz_session_id'] = session.id

        return redirect('next_question')  #
    else:
        return redirect('home')

def next_question(request):
    session_id = request.session.get('quiz_session_id')
    if not session_id:
        return redirect('home')

    session = get_object_or_404(QuizSession, id=session_id)

    if session.questions_answered >= 5:  
        return redirect('quiz_results')

    question_count = Question.objects.filter(subject=session.subject).count()
    if question_count == 0:
        return render(request, 'error.html', {'error': f'No questions available for subject {session.subject}.'})

    random_index = random.randint(0, question_count - 1)
    question = Question.objects.filter(subject=session.subject)[random_index]

    return render(request, 'question.html', {'question': question})

# Submit the Answer
def submit_answer(request):
    if request.method == 'POST':
        session_id = request.session.get('quiz_session_id')
        if not session_id:
            return redirect('home')

        session = get_object_or_404(QuizSession, id=session_id)

        question_id = request.POST.get('question_id')
        selected_option = request.POST.get('selected_option')

        if not question_id or not selected_option:
            return render(request, 'error.html', {'error': 'Invalid form submission.'})

        question = get_object_or_404(Question, id=question_id)

        # Check if the selected option is correct
        if selected_option == question.correct_option:
            print("correct answer")
            session.correct_answers += 1
        else:
            print(f"correct is {question.correct_option} and you answered {selected_option}")
            session.incorrect_answers += 1

        session.questions_answered += 1
        session.save()

        return redirect('next_question')
    else:
        return redirect('home')

# Show Quiz Results
def quiz_results(request):
    session_id = request.session.get('quiz_session_id')
    if not session_id:
        return redirect('home')

    session = get_object_or_404(QuizSession, id=session_id)

    # Store results in history
    QuizHistory.objects.create(
        user=session.user,
        subject=session.subject,
        total_questions=session.questions_answered,
        correct_answers=session.correct_answers,
        incorrect_answers=session.incorrect_answers,
    )

    request.session.pop('quiz_session_id', None)  

    return render(request, 'results.html', {
        'total_questions': session.questions_answered,
        'correct_answers': session.correct_answers,
        'incorrect_answers': session.incorrect_answers,
    })


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request, 'All fields are required.')
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose another.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()  

        messages.success(request, 'Registration successful! Please log in.')
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('profile') 
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  

    return render(request, 'login.html')

@login_required(login_url='/login/')
def profile_view(request):
    if request.user.is_authenticated:
        quiz_history = QuizHistory.objects.filter(user=request.user).order_by('-date_taken')  
        for entry in quiz_history:
            if entry.total_questions > 0:
                entry.percentage = (entry.correct_answers * 100) / entry.total_questions
            else:
                entry.percentage = 0
        return render(request, 'profile.html', {'quiz_history': quiz_history})
    else:
        return redirect('login')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')