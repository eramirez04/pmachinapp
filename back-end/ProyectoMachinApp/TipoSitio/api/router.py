from rest_framework.routers import DefaultRouter
from .views import TipoSitioModelViewSet

router_tipositio = DefaultRouter()
router_tipositio.register(prefix = 'tipositio', basename = 'tipositio', viewset = TipoSitioModelViewSet)