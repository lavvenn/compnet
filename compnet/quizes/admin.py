from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.TabularInline):  # или StackedInline для вертикального отображения
    model = Answer
    extra = 4  # количество форм для новых ответов по умолчанию
    min_num = 2  # минимум ответов

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'topic']
    list_filter = ['topic']
    inlines = [AnswerInline]
