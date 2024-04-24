from rest_framework.viewsets import ModelViewSet
from Sede.models import Sede
from .serializers import SedeSerializer

class sedeModelViewSet(ModelViewSet):
    serializer_class = SedeSerializer
    queryset = Sede.objects.all()