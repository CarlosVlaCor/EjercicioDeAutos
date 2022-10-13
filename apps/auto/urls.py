from rest_framework import routers

from apps.auto.views import AutoViewSet

router = routers.SimpleRouter()
router.register(r'autos', AutoViewSet, 'autos')
