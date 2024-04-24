from rest_framework.viewsets import ModelViewSet
from Sitio.models import Sitio
from .serializers import SitioSerializer

class sitioModelViewSet(ModelViewSet):
    serializer_class = SitioSerializer
    queryset = Sitio.objects.all()