from rest_framework import serializers

from apps.mantenimiento.models import Mantenimiento


class MantenimSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mantenimiento
        fields = '__all__'

