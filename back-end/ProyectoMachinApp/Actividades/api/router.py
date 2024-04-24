from rest_framework.routers import DefaultRouter
from Actividades.api.views import ActividadesModelViewSet

router_Actividades = DefaultRouter()

router_Actividades.register(prefix='actividades',basename='actividades',viewset=ActividadesModelViewSet)