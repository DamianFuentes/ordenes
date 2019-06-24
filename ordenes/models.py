from django.db import models
from django.utils import timezone
import os

def path_and_rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            name = instance.laboratorio+"_"+instance.entrada+"_"+str(instance.fecha)            
            # get filename
            if instance.pk:
                filename = '{}.{}'.format(name, ext)
            else:
                # set filename as random string
                filename = '{}.{}'.format(name, ext)
                # return the whole path to the file
            return os.path.join(path, filename)

        return wrapper

class Orden(models.Model):
    laboratorio = models.CharField(max_length=20)
    entrada = models.CharField(max_length=25)
    fecha = models.DateField()
    orden = models.ImageField(upload_to=path_and_rename('imgs_ordenes/'))

