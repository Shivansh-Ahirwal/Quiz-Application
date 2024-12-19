from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('start/', views.start_quiz, name='start_quiz'),  
    path('next/', views.next_question, name='next_question'),  
    path('submit/', views.submit_answer, name='submit_answer'),  
    path('results/', views.quiz_results, name='quiz_results'),  
    path('register/', views.register, name='register'),  
    path('login/', views.login_view, name='login'),  
    path('profile/', views.profile_view, name='profile'),  
    path('logout/', views.logout_view, name='logout'), 
    path('admin/', views.to_admin, name='admin'), 
]
    