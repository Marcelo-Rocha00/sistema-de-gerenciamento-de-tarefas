from django.shortcuts import render
from rest_framework import viewsets
from .models import task
from .serializers import taskSerializer

class taskViewSet(viewsets.ModelViewSet):
    class Meta:
        queryset = task.objects.all()
        serializer_class = taskSerializer

