from rest_framework.viewsets import ModelViewSet
from Centro.models import Centro
from .serializers import CentroSerializer

class centroModelViewSet(ModelViewSet):
    serializer_class = CentroSerializer
    queryset = Centro.objects.all()