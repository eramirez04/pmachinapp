from rest_framework.serializers import ModelSerializer

from detalle.models import Detalle

class detalleSerializer(ModelSerializer):
    class Meta:
        model = Detalle
        fields = ['idDetalle', 'det_fk_ficha','det_fk_variable', 'det_valor']
        