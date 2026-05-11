from django.db import models

class Topic(models.Model):

    class ComplexityChoices(models.IntegerChoices):
        BEGINNER = 1, 'Начальный'
        EASY = 2, 'Лёгкий'
        INTERMEDIATE = 3, 'Средний'
        ADVANCED = 4, 'Продвинутый'
        EXPERT = 5, 'Экспертный'


    name = models.TextField('название')
    description = models.TextField('описание')
    complexity = ComplexityChoices.choices

    def __str__(self):
        return self.name



class Lecture(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='lectures')
    text = models.TextField('краткое описание темы')

    material_file = models.FileField(upload_to='lecture_materials/', null=True, blank=True)

    def __str__(self):
        return f'Лекция для темы: {self.topic.name}'