from rest_framework import serializers
from TipoSitio.models import TipoSitio

class TipoSitioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSitio
        fields = ['tipo_sitio']
        
class TipoSitioFkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSitio
        fields = ['tipo_sitio']