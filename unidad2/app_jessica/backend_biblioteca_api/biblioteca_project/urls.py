from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('biblioteca_app.urls')),                # Rutas para la API REST
    path('interfaz/', include('biblioteca_app.urls_interfaz')),  # Rutas para la interfaz web
]
