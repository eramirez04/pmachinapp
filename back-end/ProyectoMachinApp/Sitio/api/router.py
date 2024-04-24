from rest_framework.routers import DefaultRouter
from .views import sitioModelViewSet

router_sitio = DefaultRouter()
router_sitio.register(prefix = 'sitio', basename = 'sitio', viewset = sitioModelViewSet)