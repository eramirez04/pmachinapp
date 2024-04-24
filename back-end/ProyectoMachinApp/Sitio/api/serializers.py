from rest_framework import serializers
from Sitio.models import Sitio
from Area.api.serializers import AreaFkSerializer
from TipoSitio.api.serializers import TipoSitioFkSerializer

class SitioSerializer(serializers.ModelSerializer):
    sit_fk_areas = AreaFkSerializer(read_only=True)
    sit_fk_tipo_sitio = TipoSitioFkSerializer(read_only=True)
    class Meta:
        model = Sitio
        fields = ['sit_fk_areas', 'sit_fk_tipo_sitio', 'sit_nombre']