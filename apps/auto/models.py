from django.db import models

from apps.modelo.models import Modelo
from apps.user.models import User


# Create your models here.


class Auto(models.Model):
    placa = models.CharField(verbose_name='Placa', max_length=50)
    kilometraje = models.PositiveIntegerField(verbose_name='Kilometraje', default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    modelo = models.ManyToManyField(Modelo)

    class Meta:
        verbose_name = 'Auto'
        verbose_name = 'Autos'

    def __str__(self):
        return "%s %s %s" % (self.user.first_name, self.placa, self.kilometraje)


