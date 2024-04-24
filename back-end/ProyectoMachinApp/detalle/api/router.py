from rest_framework.routers import DefaultRouter

from detalle.api.views import detalleModelViewSet

router_detalle = DefaultRouter()

router_detalle.register(prefix='detalle', basename='detalle', viewset = detalleModelViewSet)