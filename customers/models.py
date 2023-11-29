
from django.db import models


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.TextField()
    gender = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=20)
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

# Create your models here.
