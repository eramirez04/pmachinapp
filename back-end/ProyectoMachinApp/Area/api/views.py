from rest_framework.viewsets import ModelViewSet
from Area.models import Area
from .serializers import areaSerializer

class areaModelViewSet(ModelViewSet):
    serializer_class = areaSerializer
    queryset = Area.objects.all()