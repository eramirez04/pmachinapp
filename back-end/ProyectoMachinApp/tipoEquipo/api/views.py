
from rest_framework.viewsets import ModelViewSet

from tipoEquipo.models import Tipo_equipo

from tipoEquipo.api.serializer import TipoEquipoSerializer

class tipoEquipoModelViewSet(ModelViewSet):
    serializer_class = TipoEquipoSerializer
    queryset = Tipo_equipo.objects.all()
    