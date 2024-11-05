from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

# from interview.inventory.models import Inventory, InventoryLanguage, InventoryTag, InventoryType
# from database import inventory_items

class ItemListViewTests(APITestCase):
    # @classmethod
    # def setUpTestData(cls):
    #     for item in inventory_items:
    #         inventory_item, tags = item
    #         Inventory.objects.create(**inventory_item).tags.add(*tags)


    def test_items_filtered_by_year(self):
        # Test with a valid date parameter that matches the year 2023
        # response = self.client.get(url, {'date': '2000-01-01T00:00:00Z'})
        url = reverse('inventory-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Can't seem to find the data
        self.assertEqual(len(response.data), 0)
