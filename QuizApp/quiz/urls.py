from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('start/', views.start_quiz, name='start_quiz'),  # Start quiz
    path('next/', views.next_question, name='next_question'),  # Fetch next question
    path('submit/', views.submit_answer, name='submit_answer'),  # Submit answer
    path('results/', views.quiz_results, name='quiz_results'),  # Display results
]
    