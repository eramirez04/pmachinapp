from rest_framework import serializers
from Sede.models import Sede
from Centro.api.serializers import CentroFkSerializer

class SedeSerializer(serializers.ModelSerializer):
    sede_fk_centros = CentroFkSerializer(read_only=True)
    class Meta:
        model = Sede
        fields = ['sede_fk_centros' ,'sede_nombre', 'sede_descripcion', 'sede_direccion']
        
class SedeFkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = ['sede_nombre']