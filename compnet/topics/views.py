from django.shortcuts import render, get_object_or_404

from topics import models


def list_of_topics(request):

    template = "topics/topic_list.html"

    all_topics = models.Topic.objects.all()

    return render(request, template, {"topics": all_topics})


def topic_ditail(request, pk):
    template = 'topics/topic_page.html'

    topic = get_object_or_404(models.Topic, pk = pk)

    return render(request, template, {"topic": topic})
