# inventory/urls.py

from django.urls import path
from .views import add_good, deduct_good, update_good, get_all_goods, get_good_by_id

urlpatterns = [
    path('add/', add_good, name='add_good'),
    path('deduct/<int:good_id>/', deduct_good, name='deduct_good'),
    path('update/<int:good_id>/', update_good, name='update_good'),
    path('all/', get_all_goods, name='get_all_goods'),
    path('<int:good_id>/', get_good_by_id, name='get_good_by_id'),
]
