from rest_framework.viewsets import ModelViewSet
from tipo_mantenimiento.models import tipo_mantenimiento_models
from tipo_mantenimiento.api.serializers import Tipo_mantenimiento_Serializer

class tipo_mantenimiento_ModelViewSet(ModelViewSet):
    serializer_class = Tipo_mantenimiento_Serializer
    queryset = tipo_mantenimiento_models.objects.all()