from rest_framework.serializers import ModelSerializer

from ficha.models import Ficha

class fichaSerializer(ModelSerializer):
    class Meta:
        model = Ficha
        fields = ['idFichas', 'fi_fecha', 'fi_placa_sena', 'fi_serial', 'fi_fecha_adquisicion', 'fi_fecha_inicioGarantia', 'fi_fecha_finGarantia', 'fi_descripcionGarantia', 'fi_imagen', 'fi_estado','fi_fk_tipoFicha' ]