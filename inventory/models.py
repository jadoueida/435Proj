
from django.db import models


class Good(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    count_in_stock = models.IntegerField()

    def __str__(self):
        return self.name
