from rest_framework.viewsets import ModelViewSet
from Actividades.models import Actividades
from Actividades.api.serializers import ActividadesSerializer

class ActividadesModelViewSet(ModelViewSet):
    serializer_class = ActividadesSerializer
    queryset = Actividades.objects.all()
    http_method_name = ['get', 'put']