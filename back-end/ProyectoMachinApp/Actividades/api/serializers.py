from rest_framework.serializers import ModelSerializer
from Actividades.models import Actividades

class ActividadesSerializer(ModelSerializer):
    class Meta:
        model=Actividades
        fields=['idActividades','acti_nombre','acti_descripcion','acti_fecha_realizacion','acti_estado','fk_mantenimiento']