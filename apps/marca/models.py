from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=50)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.nombre
