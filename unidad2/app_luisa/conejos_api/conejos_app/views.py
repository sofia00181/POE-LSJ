from rest_framework import viewsets
from .models import Conejo
from .serializers import ConejoSerializer

class ConejoViewSet(viewsets.ModelViewSet):
    queryset = Conejo.objects.all()
    serializer_class = ConejoSerializer
