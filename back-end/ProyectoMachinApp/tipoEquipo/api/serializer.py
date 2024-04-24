from rest_framework.serializers import ModelSerializer


from tipoEquipo.models import Tipo_equipo

class TipoEquipoSerializer(ModelSerializer):
    class Meta:
        model = Tipo_equipo

        fields = '__all__'
