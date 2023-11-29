# sales/urls.py

from django.urls import path
from .views import display_available_goods, get_good_details, make_sale, get_customer_sales_history

urlpatterns = [
    path('display_available_goods/', display_available_goods, name='display_available_goods'),
    path('get_good_details/<int:good_id>/', get_good_details, name='get_good_details'),
    path('make_sale/', make_sale, name='make_sale'),
    path('sales_history/<str:customer_username>/', get_customer_sales_history, name='get_customer_sales_history'),
]
