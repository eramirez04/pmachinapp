from rest_framework.viewsets import ModelViewSet

from ficha.models import Ficha

from ficha.api.serializer import fichaSerializer


class fichaModelViewSet(ModelViewSet):
    serializer_class = fichaSerializer
    queryset = Ficha.objects.all()