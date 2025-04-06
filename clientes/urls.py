from django.urls import path, include
from rest_framework import routers
from .views import ComputadorViewSet

router = routers.DefaultRouter()
router.register(r'computadores', ComputadorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
