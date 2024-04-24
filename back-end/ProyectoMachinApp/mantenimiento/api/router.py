from rest_framework.routers import DefaultRouter
from mantenimiento.api.views import mantenimiento_ModelViewSet

router_mantenimiento = DefaultRouter()
router_mantenimiento.register(prefix = 'mantenimiento', basename = 'mantenimiento', viewset = mantenimiento_ModelViewSet)