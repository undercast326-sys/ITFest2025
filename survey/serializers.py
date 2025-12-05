from rest_framework import serializers
from .models import Questions, Choice


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields ='__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer

    class Meta:
        model = Choice
        fields ='__all__'