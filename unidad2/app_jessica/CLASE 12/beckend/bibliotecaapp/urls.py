from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BibliotecaViewSet
   
router = DefaultRouter()
router.register(r'biblioteca', BibliotecaViewSet)

urlpatterns = [
       path('', include(router.urls)),
   ]