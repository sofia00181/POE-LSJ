from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConejoViewSet

router = DefaultRouter()
router.register(r'conejos', ConejoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
