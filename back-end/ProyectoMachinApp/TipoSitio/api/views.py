from rest_framework.viewsets import ModelViewSet
from TipoSitio.models import TipoSitio
from TipoSitio.api.serializers import TipoSitioSerializer

class TipoSitioModelViewSet(ModelViewSet):
    serializer_class = TipoSitioSerializer
    queryset = TipoSitio.objects.all()