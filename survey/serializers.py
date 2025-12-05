from rest_framework import serializers
from .models import Questions, Choice, SurveyResponse


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields ='__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer

    class Meta:
        model = Choice
        fields ='__all__'


class SurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = ('id', 'responses_data', 'completed_at', 'ai_analysis')
        read_only_fields = ('id', 'completed_at', 'ai_analysis')
