from webapp import serializers
from webapp import models
from webapp.permissions import IsModeratorOrReadOnly
from rest_framework import viewsets


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = models.University.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = serializers.UniversitySerializer
    permission_classes = [IsModeratorOrReadOnly]


class MajorViewSet(viewsets.ModelViewSet):
    queryset = models.Major.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = serializers.MajorSerializer
    permission_classes = [IsModeratorOrReadOnly]


class TypeViewSet(viewsets.ModelViewSet):
    queryset = models.Type.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = serializers.TypeSerializer
    permission_classes = [IsModeratorOrReadOnly]
