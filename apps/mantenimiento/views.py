from django.shortcuts import render
from rest_framework import viewsets

from apps.mantenimiento.models import Mantenimiento
from apps.mantenimiento.serializers import MantenimSerializer
from apps.user.models import User


# Create your views here.
class MantenimientoViewSet(viewsets.ModelViewSet):
    serializer_class = MantenimSerializer
    #

