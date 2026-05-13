from django.db import models

from topics.models import Topic

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст вопроса')


    def __str__(self):
        return f"{self.topic.name} {self.text[:50] + '...' if len(self.text) > 50 else self.text}"


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Вопрос'
    )
    text = models.CharField(max_length=500, verbose_name='Текст ответа')
    is_correct = models.BooleanField(default=False, verbose_name='Правильный ответ')

    def __str__(self):
        return f"{self.text} ({'✓' if self.is_correct else '✗'})"
