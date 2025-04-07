from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComputadorViewSet

router = DefaultRouter()
router.register(r'computador', ComputadorViewSet)

urlpatterns = [
    path('', include(router.urls))
]