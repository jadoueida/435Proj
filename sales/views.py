# sales/views.py

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from customers.models import Customer
from inventory.models import Good
from .models import Sale
import json


@require_GET
def display_available_goods(request):
    goods = Good.objects.filter(count_in_stock__gt=0)
    goods_list = [{"name": g.name, "price_per_item": str(g.price_per_item)} for g in goods]
    return JsonResponse({"available_goods": goods_list})


@require_GET
def get_good_details(request, good_id):
    good = get_object_or_404(Good, id=good_id)
    return JsonResponse({
        "id": good.id,
        "name": good.name,
        "category": good.category,
        "price_per_item": str(good.price_per_item),
        "description": good.description,
        "count_in_stock": good.count_in_stock,
    })


@csrf_exempt
@require_POST
def make_sale(request):
    data = json.loads(request.body)
    good_name = data.get("good_name")
    customer_username = data.get("customer_username")

    try:
        customer = Customer.objects.get(username=customer_username)
        good = Good.objects.get(name=good_name, count_in_stock__gt=0)

        if customer.wallet_balance >= good.price_per_item:

            customer.wallet_balance -= good.price_per_item
            customer.save()

            good.count_in_stock -= 1
            good.save()

            Sale.objects.create(customer=customer, good=good)

            return JsonResponse({"message": "Sale completed successfully"})
        else:
            return JsonResponse({"error": "Insufficient funds"}, status=400)
    except Customer.DoesNotExist:
        return JsonResponse({"error": "Customer not found"}, status=404)
    except Good.DoesNotExist:
        return JsonResponse({"error": "Good not found or out of stock"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@require_GET
def get_customer_sales_history(request, customer_username):
    customer = get_object_or_404(Customer, username=customer_username)
    sales = Sale.objects.filter(customer=customer)
    sales_list = [{"good_name": sale.good.name, "sale_date": str(sale.sale_date)} for sale in sales]
    return JsonResponse({"sales_history": sales_list})
