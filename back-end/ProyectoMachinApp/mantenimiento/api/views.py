from rest_framework.viewsets import ModelViewSet
from mantenimiento.models import mantenimiento_models
from mantenimiento.api.serializers import mantenimiento_Serializer

class mantenimiento_ModelViewSet(ModelViewSet):
    serializer_class = mantenimiento_Serializer
    queryset = mantenimiento_models.objects.all()