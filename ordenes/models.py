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

class Orden(models.Model):
    laboratorio = models.CharField(max_length=20)
    entrada = models.CharField(max_length=25)
    fecha = models.DateField()
    orden = models.ImageField(upload_to=path_and_rename)

