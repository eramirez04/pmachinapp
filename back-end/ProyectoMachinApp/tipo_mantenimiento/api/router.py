from rest_framework.routers import DefaultRouter
from tipo_mantenimiento.api.views import tipo_mantenimiento_ModelViewSet

router_movimiento = DefaultRouter()
router_movimiento.register(prefix = 'movimiento', basename = 'movimiento', viewset = tipo_mantenimiento_ModelViewSet)