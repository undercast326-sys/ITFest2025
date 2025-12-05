from .models import Questions, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework import viewsets
from webapp import permissions

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Questions.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = [permissions.IsModeratorOrReadOnly]


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = [permissions.IsModeratorOrReadOnly]
