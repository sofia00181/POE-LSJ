from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Computador
from .serializers import ComputadorSerializer

class ComputadorViewSet(viewsets.ModelViewSet):
    queryset = Computador.objects.all()
    serializer_class = ComputadorSerializer
