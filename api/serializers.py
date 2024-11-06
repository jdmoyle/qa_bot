from rest_framework import serializers
from .models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Question model to convert the question data to JSON format.
    """
    class Meta:
        model = Question
        fields = ['id', 'text']  # Include only the necessary fields


class AnswerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Answer model to convert the answer data to JSON format.
    """
    question = QuestionSerializer()  # Embed the question details in the answer response

    class Meta:
        model = Answer
        fields = ['id', 'question', 'answer_text']  # Include the necessary fields
