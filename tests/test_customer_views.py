import json
from django.test import TestCase, Client
from customers.models import Customer

class CustomerViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_customer(self):
        data = {
            "full_name": "John Doe",
            "username": "john_doe",
            "age": 30,
            "address": "123 Main St",
            "gender": "Male",
            "marital_status": "Single",
            "wallet_balance": 100.0,
        }

        response = self.client.post('/customers/register/', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertIn("id", response.json())

    def test_manage_customer_get(self):
        customer = Customer.objects.create(
            full_name="Jane Doe",
            username="jane_doe",
            age=25,
            address="456 Oak St",
            gender="Female",
            marital_status="Married",
            wallet_balance=50.0,
        )

        response = self.client.get(f'/customers/{customer.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())

    def test_manage_customer_delete(self):
        customer = Customer.objects.create(
            full_name="Jane Doe",
            username="jane_doe",
            age=25,
            address="456 Oak St",
            gender="Female",
            marital_status="Married",
            wallet_balance=50.0,
        )

        response = self.client.delete(f'/customers/{customer.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_charge_customer(self):
        customer = Customer.objects.create(
            full_name="Jane Doe",
            username="jane_doe",
            age=25,
            address="456 Oak St",
            gender="Female",
            marital_status="Married",
            wallet_balance=50,
        )

        data = {"username": "jane_doe", "amount": 30}
        response = self.client.post('/customers/charge/', json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertIn("new_balance", response.json())

    def test_deduct_money(self):
        customer = Customer.objects.create(
            full_name="Jane Doe",
            username="jane_doe",
            age=25,
            address="456 Oak St",
            gender="Female",
            marital_status="Married",
            wallet_balance=50,
        )

        data = {"username": "jane_doe", "amount": 30}
        response = self.client.post('/customers/deduct/', json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertIn("new_balance", response.json())

    def test_get_all_customers(self):
        Customer.objects.create(
            full_name="John Doe",
            username="john_doe",
            age=30,
            address="123 Main St",
            gender="Male",
            marital_status="Single",
            wallet_balance=100.0,
        )
        Customer.objects.create(
            full_name="Jane Doe",
            username="jane_doe",
            age=25,
            address="456 Oak St",
            gender="Female",
            marital_status="Married",
            wallet_balance=50.0,
        )

        response = self.client.get('/customers/all/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("customers", response.json())

    def test_get_customer_by_username(self):
        customer = Customer.objects.create(
            full_name="John Doe",
            username="john_doe",
            age=30,
            address="123 Main St",
            gender="Male",
            marital_status="Single",
            wallet_balance=100.0,
        )

        response = self.client.get(f'/customers/{customer.username}/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json())

