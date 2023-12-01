import json
from django.test import TestCase, Client
from django.urls import reverse
from customers.models import Customer
from inventory.models import Good
from sales.models import Sale

class SalesViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.customer = Customer.objects.create(username="test_customer", age=25, wallet_balance=100.0)
        self.good = Good.objects.create(name="Test Good", category="Test Category", price_per_item=10.99, count_in_stock=5)


    def test_display_available_goods(self):
        url = reverse('display_available_goods')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("available_goods" in response.json())

    def test_get_good_details(self):
        url = reverse('get_good_details', args=[self.good.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("id" in response.json())
        self.assertEqual(response.json().get("id"), self.good.id)

    def test_make_sale(self):
        url = reverse('make_sale')
        data = {"good_name": self.good.name, "customer_username": self.customer.username}
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Sale completed successfully", response.json().get("message"))

    def test_get_customer_sales_history(self):
        Sale.objects.create(customer=self.customer, good=self.good)
        url = reverse('get_customer_sales_history', args=[self.customer.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("sales_history" in response.json())
