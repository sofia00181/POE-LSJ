from django.db import models

# Create your models here.

from django.db import models

class Computador(models.Model):
    teclado = models.CharField(max_length=100)
    mouse = models.CharField(max_length=100)
    pantalla = models.CharField(max_length=100)
    software = models.CharField(max_length=100)

    def __str__(self):
     return self.teclado

