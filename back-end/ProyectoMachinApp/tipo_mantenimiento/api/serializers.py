from rest_framework import serializers
from tipo_mantenimiento.models import tipo_mantenimiento_models

class Tipo_mantenimiento_Serializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_mantenimiento_models
        fields = ['tipo_mantenimiento']