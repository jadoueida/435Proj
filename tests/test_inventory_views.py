# inventory/tests/test_views.py
import json
from django.test import TestCase, Client
from django.urls import reverse
from inventory.models import Good

class InventoryViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_add_good(self):
        url = reverse('add_good')
        data = {"name": "Test Good", "category": "Test Category", "price_per_item": 10.99, "count_in_stock": 5}
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Good added successfully", response.json().get("message"))
        self.assertTrue("id" in response.json())

    def test_deduct_good(self):
        good = Good.objects.create(name="Test Good", category="Test Category", price_per_item=10.99, count_in_stock=5)
        url = reverse('deduct_good', args=[good.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Good deducted successfully", response.json().get("message"))
        self.assertTrue("new_count_in_stock" in response.json())

    def test_update_good(self):
        good = Good.objects.create(name="Test Good", category="Test Category", price_per_item=10.99, count_in_stock=5)
        url = reverse('update_good', args=[good.id])
        data = {"name": "Updated Good", "price_per_item": 15.99}
        response = self.client.put(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Good updated successfully", response.json().get("message"))

    def test_get_all_goods(self):
        url = reverse('get_all_goods')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("goods" in response.json())

    def test_get_good_by_id(self):
        good = Good.objects.create(name="Test Good", category="Test Category", price_per_item=10.99, count_in_stock=5)
        url = reverse('get_good_by_id', args=[good.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("id" in response.json())
        self.assertEqual(response.json().get("id"), good.id)

