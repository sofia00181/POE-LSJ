from django.db import models

# Create your models here.
class Computador(models.Model):
    teclado = models.CharField(max_length=100)
    mouse = models.CharField(max_length=100)
    pantalla = models.CharField(max_length=100)
    software = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teclado