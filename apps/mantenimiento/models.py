from django.db import models

from apps.auto.models import Auto


# Create your models here.


class Mantenimiento(models.Model):
    kilometraje = models.PositiveIntegerField(verbose_name="Kilometraje", default=0)
    descripcion = models.CharField(verbose_name='decripcion', max_length=250)
    costo = models.PositiveIntegerField(verbose_name='Costo', default=0)
    fecha = models.DateField(verbose_name='Fecha')
    auto = models.ManyToManyField(Auto)

    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'

    def __str__(self):
        return "%s %s %s, %s" % (self.kilometraje, self.descripcion, self.costo, self.auto.placa)
