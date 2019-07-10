from django.db import models
from django.utils import timezone
from django.utils.deconstruct import deconstructible

import os

@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        name = instance.laboratorio+"_"+instance.entrada+"_"+str(instance.fecha)            
        filename = '{}.{}'.format(name, ext)
        return os.path.join(self.path, filename)

path_and_rename = PathAndRename('imgs_ordenes/')

class OrdenPapel(models.Model):
    laboratorio = models.CharField(max_length=20)
    entrada = models.CharField(max_length=25)
    fecha = models.DateField()
    orden = models.ImageField(upload_to=path_and_rename)

class OrdenSistema(models.Model):
    laboratorio = models.CharField(max_length=20)
    entrada = models.CharField(max_length=25)
    fechaRegistro = models.DateField()
    fechaSubido = models.DateField(blank=True, null=True)
    fechaPrescripcion = models.DateField(blank=True, null=True)
    diagnostico = models.CharField(max_length=250, blank=True, null=True)
    prescriptor = models.CharField(max_length=100)
    paciente = models.CharField(max_length=100)
    items = models.CharField(max_length=2000)
    descargado = models.BooleanField(default=False)
    editado = models.BooleanField(default=False)

class Picture(models.Model):
    image = models.ImageField()

class Usuario(models.Model):
    laboratorios = models.CharField(max_length=200)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    colegio = models.CharField(max_length=100)
    usuario = models.CharField(max_length=50)