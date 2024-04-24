from rest_framework.routers import DefaultRouter
from .views import areaModelViewSet

router_area = DefaultRouter()
router_area.register(prefix = 'area', basename = 'area', viewset = areaModelViewSet)