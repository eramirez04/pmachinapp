from rest_framework import serializers
from mantenimiento.models import mantenimiento_models
from tipo_mantenimiento.api.serializers import Tipo_mantenimiento_Serializer

class mantenimiento_Serializer(serializers.ModelSerializer):
    mant_fk_mantenimiento = Tipo_mantenimiento_Serializer(""" read_only=True """)
    class Meta:
        model = mantenimiento_models
        fields = ['mant_codigo_mantenimiento', 'mant_fecha_realizacion', 'mant_fecha_proxima', 'mant_fk_mantenimiento', 'mant_descripcion']