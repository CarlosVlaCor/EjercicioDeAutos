from django.db import models

from apps.marca.models import Marca


# Create your models here.
class Modelo(models.Model):
    nombre = models.CharField(verbose_name= 'Nombre', max_length=50)
    marca = models.ManyToManyField(Marca)

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self):
        return "%s %s" % (self.nombre, self.marca)
