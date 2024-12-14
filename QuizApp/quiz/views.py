from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, QuizSession
from django.db.models import Count
import random

# Home Page
def home(request):
    return render(request, 'home.html')

def start_quiz(request):
    # End all previous sessions for the user
    QuizSession.objects.filter(user="User1").delete()

    # Create a new session
    session = QuizSession.objects.create(user="User1")

    # Store the new session ID in the user's session
    request.session['quiz_session_id'] = session.id

    return redirect('next_question')

# Get a Random Question
def next_question(request):
    session_id = request.session.get('quiz_session_id')
    if not session_id:
        return redirect('home')

    session = get_object_or_404(QuizSession, id=session_id)

    if session.questions_answered >= 5:  # Set a limit of 5 questions
        return redirect('quiz_results')

    # Fetch a random question
    question_count = Question.objects.aggregate(count=Count('id'))['count']
    if question_count == 0:
        return render(request, 'error.html', {'error': 'No questions available in the database.'})

    random_index = random.randint(0, question_count - 1)
    question = Question.objects.all()[random_index]

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
    request.session.pop('quiz_session_id', None)  # Clear session on results display

    return render(request, 'results.html', {
        'total_questions': session.questions_answered,
        'correct_answers': session.correct_answers,
        'incorrect_answers': session.incorrect_answers
    })
