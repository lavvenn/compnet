from django.urls import path

from topics import views

app_name = 'topics'

urlpatterns = [
    path('list', views.list_of_topics, name='topic_list'),
    path('<int:pk>', views.topic_ditail, name='topic'),
]