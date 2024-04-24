from rest_framework.routers import DefaultRouter
from .views import centroModelViewSet

router_centro = DefaultRouter()
router_centro.register(prefix = 'centro', basename = 'centro', viewset = centroModelViewSet)