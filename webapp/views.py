from webapp import serializers
from webapp import models
from webapp.models import University
from webapp.permissions import IsModeratorOrReadOnly
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404


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


def index(request):
    return render(request, 'webapp/index.html')

def university_detail(request, pk):
    university = get_object_or_404(University, pk=pk)
    return render(request, 'webapp/university_detail.html', {'university_id': pk})
