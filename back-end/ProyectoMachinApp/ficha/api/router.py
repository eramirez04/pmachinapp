from rest_framework.routers import DefaultRouter

from ficha.api.views import fichaModelViewSet

router_ficha = DefaultRouter()

router_ficha.register(prefix='ficha', basename = 'ficha', viewset=fichaModelViewSet)