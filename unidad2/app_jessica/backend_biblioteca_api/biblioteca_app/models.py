from django.db import models

class Material(models.Model):
    titulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    anio = models.IntegerField()

    def __str__(self):
        return self.titulo