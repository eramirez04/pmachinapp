from rest_framework.viewsets import ModelViewSet

from variable.models import Variable

from variable.api.serializer import variableSerializer

class variableModelViewSet(ModelViewSet):
    serializer_class = variableSerializer
    queryset = Variable.objects.all()

    