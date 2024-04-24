from rest_framework.routers import DefaultRouter

from variable.api.views import variableModelViewSet


router_variable = DefaultRouter()

router_variable.register(prefix='variable', basename='variable', viewset = variableModelViewSet )