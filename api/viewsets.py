from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAdminUser

from api.serializers import VPSSerializer
from vps.models import VPS


class VPSViewSet(viewsets.ModelViewSet):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ("status", "cpu", "ram", "hdd")
    ordering_fields = ("uid", "cpu", "ram", "hdd", "status")
