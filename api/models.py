from django.db import models


class Question(models.Model):
    """
    Model for storing questions that will be asked based on a document.
    """
    text = models.CharField(max_length=500, help_text="The question text.")

    def __str__(self):
        return self.text


class Answer(models.Model):
    """
    Model for storing answers to the questions based on the document content.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.TextField(help_text="The answer text.")

    def __str__(self):
        return f"Answer to: {self.question.text}"
