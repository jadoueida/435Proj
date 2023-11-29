# customers/urls.py

from django.urls import path
from .views import register_customer, manage_customer, charge_customer, deduct_money, get_all_customers, get_customer_by_username

urlpatterns = [
    path('register/', register_customer, name='register_customer'),
    path('<int:customer_id>/', manage_customer, name='manage_customer'),
    path('charge/', charge_customer, name='charge_customer'),
    path('deduct/', deduct_money, name='deduct_money'),
    path('all/', get_all_customers, name='get_all_customers'),
    path('<str:username>/', get_customer_by_username, name='get_customer_by_username'),
]
