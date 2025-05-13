from django.db import models

class Biblioteca(models.Model):
    titulo = models.CharField(max_length= 100)
    categoria = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    año = models.IntegerField()

def __str__(self):
    return f'{self.titulo} - {self.categoria} - {self.autor} - {self.año}'