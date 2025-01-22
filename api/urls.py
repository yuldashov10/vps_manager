from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.apps import ApiConfig
from api.viewsets import VPSViewSet

app_name = ApiConfig.name

router_v1 = DefaultRouter()
router_v1.register(r"vps", VPSViewSet, basename="vps")

urlpatterns = [
    path("", include(router_v1.urls)),
]
