from rest_framework import serializers
from Area.models import Area
from Sede.api.serializers import SedeFkSerializer

class areaSerializer(serializers.ModelSerializer):
    area_fk_sedes = SedeFkSerializer(read_only=True)
    class Meta:
        model = Area
        fields = ['area_fk_sedes', 'area_nombre']
        
class AreaFkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['area_nombre']