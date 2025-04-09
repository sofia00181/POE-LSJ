from django.urls import path, include

urlpatterns = [
    path('api/', include('biblioteca_app.urls')),
]