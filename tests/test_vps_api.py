from typing import Any

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from vps.models import VPS, StatusVPS


class VPSTestCase(APITestCase):
    def setUp(self):
        self.vps1 = VPS.objects.create(
            cpu=4,
            ram=4096,
            hdd=100,
            status=StatusVPS.STARTED,
        )
        self.vps2 = VPS.objects.create(
            cpu=2,
            ram=2048,
            hdd=50,
            status=StatusVPS.STOPPED,
        )

        self.admin_user = User.objects.create_superuser(
            email="test_admin@example.com",
            password="test_password_for_admin123",
        )

        self.admin_user_token = str(
            RefreshToken.for_user(self.admin_user).access_token
        )
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.admin_user_token}",
        )

        self.list_url = reverse("api:vps-list")
        self.detail_url = lambda uid: reverse(
            "api:vps-detail",
            args=[uid],
        )

    def test_create_vps(self):
        data: dict[str, Any] = {
            "cpu": 8,
            "ram": 8192,
            "hdd": 200,
            "status": StatusVPS.STARTED,
        }

        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VPS.objects.count(), 3)
        self.assertEqual(response.data["cpu"], data["cpu"])

    def test_get_vps_by_uid(self):
        response = self.client.get(self.detail_url(self.vps1.uid))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["uid"], str(self.vps1.uid))

    def test_list_vps(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_filter_vps_by_status(self):
        response = self.client.get(
            self.list_url, {"status": StatusVPS.STARTED}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(
            response.data["results"][0]["status"],
            StatusVPS.STARTED,
        )

    def test_update_vps(self):
        data: dict[str, Any] = {
            "cpu": 6,
            "ram": 6144,
            "hdd": 120,
            "status": StatusVPS.BLOCKED,
        }

        response = self.client.put(
            self.detail_url(self.vps1.uid),
            data,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.vps1.refresh_from_db()

        self.assertEqual(self.vps1.cpu, data["cpu"])
        self.assertEqual(self.vps1.status, StatusVPS.BLOCKED)

    def test_delete_vps(self):
        response = self.client.delete(self.detail_url(self.vps1.uid))

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertEqual(VPS.objects.count(), 1)

    def test_unauthenticated_access(self):
        self.client.credentials()
        response = self.client.get(self.list_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
        )
