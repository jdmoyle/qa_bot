from django.urls import path
from .views import QuestionAnsweringAPIView

urlpatterns = [
    path('answer-questions/', QuestionAnsweringAPIView.as_view(), name='answer_questions'),
]
