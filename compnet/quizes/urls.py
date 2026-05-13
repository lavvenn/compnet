from django.urls import path
from . import views

app_name = 'quizes'

urlpatterns = [
    path('<int:topic_id>/test/', views.test_view, name='test_view'),
    path('submit-test/', views.submit_test, name='submit_test'),
]
