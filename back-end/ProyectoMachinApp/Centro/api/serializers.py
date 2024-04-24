from rest_framework import serializers
from Centro.models import Centro

class CentroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centro
        fields = ['cen_nombre', 'cen_descripcion', 'cen_regional', 'cen_municipio', 'cen_subdirector']
        
class CentroFkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centro
        fields = ['cen_nombre']