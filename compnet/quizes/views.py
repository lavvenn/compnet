from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from topics.models import Topic
from quizes.models import Question, Answer
import random

def test_view(request, topic_id):
    # Получаем тему
    topic = get_object_or_404(Topic, id=topic_id)

    # Берём 10 случайных вопросов по теме
    all_questions = list(Question.objects.filter(topic=topic))
    if len(all_questions) < 10:
        # Если вопросов меньше 10, берём все
        selected_questions = all_questions
    else:
        selected_questions = random.sample(all_questions, 10)

    context = {
        'topic': topic,
        'questions': selected_questions,
    }
    return render(request, 'quizes/quiz.html', context)

def submit_test(request):
    if request.method == 'POST':
        score = 0
        total_questions = 0
        topic_id = None  # будем сохранять ID темы

        for key, value in request.POST.items():
            if key.startswith('question_'):
                total_questions += 1
                question_id = key.split('_')[1]
                selected_answer_id = value


                try:
                    # Получаем вопрос, чтобы извлечь topic_id
                    question = Question.objects.get(id=question_id)
                    topic_id = question.topic.id
                    selected_answer = Answer.objects.get(id=selected_answer_id)
                    if selected_answer.is_correct:
                        score += 1
                except (Question.DoesNotExist, Answer.DoesNotExist):
                    pass

        percentage = (score / total_questions * 100) if total_questions > 0 else 0

        context = {
            'score': score,
            'total': total_questions,
            'percentage': percentage,
            'topic_id': topic_id,  # передаём ID темы в шаблон
        }
        return render(request, 'quizes/quiz_result.html', context)
    return HttpResponseRedirect('/')

