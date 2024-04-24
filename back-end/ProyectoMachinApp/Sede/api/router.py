from rest_framework.routers import DefaultRouter
from .views import sedeModelViewSet

router_sede = DefaultRouter()
router_sede.register(prefix = 'sede', basename = 'sede', viewset = sedeModelViewSet)