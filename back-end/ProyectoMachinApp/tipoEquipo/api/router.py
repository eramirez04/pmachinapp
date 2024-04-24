from rest_framework.routers import DefaultRouter

from tipoEquipo.api.views import tipoEquipoModelViewSet


router_tipoEquipo = DefaultRouter()

router_tipoEquipo.register(prefix='equipo', basename='equipo', viewset =tipoEquipoModelViewSet )