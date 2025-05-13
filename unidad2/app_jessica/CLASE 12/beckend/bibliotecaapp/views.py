from rest_framework import viewsets
from .models import Biblioteca
from .serializers import BibliotecaSerializer 

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer