from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.admin import User
from rest_framework.permissions import IsAuthenticated

from apps.auto.models import Auto
from apps.auto.permissions import IsAdmin
from apps.auto.serializers import AutoSerializer
from apps.user.permissions import IsCliente


# Create your views here.
class AutoViewSet(viewsets.ModelViewSet):
    serializer_class = AutoSerializer
    #queryset = Auto.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'delete',
                           'set_password']:
            permission_classes = (IsAuthenticated, IsAdmin)
        elif self.action in ['list', 'retrieve']:
            permission_classes = (IsAuthenticated, IsAdmin | IsCliente)
        else:
            permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Auto.objects.all()
        user = self.request.user
        if user.type == User.Type.CLIENTE:
            queryset = queryset.filter(user=user)

        return queryset

