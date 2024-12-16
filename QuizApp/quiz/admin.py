from django.contrib import admin
from .models import Question, QuizSession, QuizHistory

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'subject', 'option_a', 'option_b', 'option_c', 'option_d', 'get_correct_option')
    search_fields = ('text', 'subject', 'option_a', 'option_b', 'option_c', 'option_d')
    list_filter = ('subject',)

    def get_correct_option(self, obj):
        return obj.get_correct_option_display()
    get_correct_option.short_description = 'Correct Option' 


@admin.register(QuizSession)
class QuizSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'questions_answered', 'correct_answers', 'incorrect_answers', 'start_time', 'end_time')
    search_fields = ('user__username', 'subject') 
    list_filter = ('subject', 'start_time') 
    readonly_fields = ('start_time', 'end_time')


@admin.register(QuizHistory)
class QuizHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'total_questions', 'correct_answers', 'incorrect_answers', 'date_taken')
    search_fields = ('user__username', 'subject') 
    list_filter = ('subject', 'date_taken')  
    readonly_fields = ('date_taken',) 
