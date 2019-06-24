from django.db import models
from django.utils import timezone


class Orden(models.Model):
    laboratorio = models.CharField(max_length=20)
    entrada = models.CharField(max_length=25)
    fecha = models.DateTimeField(
            blank=True, null=True)
    orden = models.CharField(max_length=25) #Luego cambiar por archivo tipo File

    def __str__(self):
        return self.entrada