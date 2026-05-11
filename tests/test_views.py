from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from restaurant.models import Booking, Menu



class MenuViewTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="menuuser",
            password="testpass123"
        )

        self.menu = Menu.objects.create(
            title="Pizza",
            price=400,
            inventory=12
        )

        self.list_url = reverse("menu-list")
        self.detail_url = reverse("menu_details", args=[self.menu.id])

    def test_menu_list_public(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_menu_retrieve_public(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

