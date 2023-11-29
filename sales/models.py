# sales/models.py

from django.db import models
from customers.models import Customer
from inventory.models import Good


class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} - {self.good.name} - {self.sale_date}"

