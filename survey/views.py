from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response

from webapp.models import University
from .models import Questions, Choice, SurveyResponse
from .serializers import QuestionSerializer, ChoiceSerializer, SurveyResponseSerializer
from rest_framework import viewsets, status
from webapp import permissions
from .services import AIAnalyzer


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Questions.objects.all()
    lookup_url_kwarg = 'id'

    @action(detail=False, methods=['post'], url_path='submit')
    def submit_survey(self, request):
        serializer = SurveyResponseSerializer(data={
            'response_data':request.data
        })

        if serializer.is_valid():
            survey_response = serializer.save()

            try:
                universities = University.objects.all()

                analyzer = AIAnalyzer()
                ai_result = analyzer.analyze_survey_responses(
                    responses_data=survey_response.responses_data,
                    universities=universities
                )

                survey_response.ai_analysis = ai_result
                survey_response.save()

                return Response({
                    'message': 'Ответы сохранены и проанализированы!',
                    'response_id': survey_response.id,
                    'analysis': ai_result
                }, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({
                    'message': 'Ответы сохранены, но анализ не удался',
                    'response_id': survey_response.id,
                    'error': str(e)
                }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='result/(?P<response_id>[^/.]+)')
    def get_result(self, request, response_id=None):
        try:
            response = SurveyResponse.objects.get(id=response_id)
            serializer = SurveyResponseSerializer(response)
            return Response(serializer.data)
        except SurveyResponse.DoesNotExist:
            return Response({
                'error': 'Answer Not Found'
            }, status=status.HTTP_404_NOT_FOUND)



class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
    lookup_url_kwarg = 'id'

def survey(request):
    return render(request, 'survey/survey.html')
