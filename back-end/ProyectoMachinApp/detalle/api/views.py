from rest_framework.viewsets import ModelViewSet

from detalle.models import Detalle

from detalle.api.serializer import detalleSerializer

class detalleModelViewSet(ModelViewSet):
    serializer_class = detalleSerializer
    queryset = Detalle.objects.all()
    