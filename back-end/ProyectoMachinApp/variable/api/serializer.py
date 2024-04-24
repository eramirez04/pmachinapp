from rest_framework.serializers import ModelSerializer

from variable.models import Variable

class variableSerializer(ModelSerializer):
    class Meta:
        model = Variable
        fields = ['idVariable', 'var_nombre', 'var_descripcion','var_fk_tipo_ficha']
