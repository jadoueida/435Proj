# customers/views.py

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods
import json

from .models import Customer

@csrf_exempt
@require_POST
def register_customer(request):
    data = json.loads(request.body)
    try:
        customer = Customer.objects.create(**data)
        return JsonResponse({"message": "Customer registered successfully", "id": customer.id})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@require_http_methods(["GET", "DELETE"])
def manage_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == "GET":
        return JsonResponse({
            "id": customer.id,
            "full_name": customer.full_name,
            "username": customer.username,
            "age": customer.age,
            "address": customer.address,
            "gender": customer.gender,
            "marital_status": customer.marital_status,
            "wallet_balance": str(customer.wallet_balance),
        })
    elif request.method == "DELETE":
        customer.delete()
        return JsonResponse({"message": "Customer deleted successfully"})

@csrf_exempt
@require_POST
def charge_customer(request):
    data = json.loads(request.body)
    username = data.get("username")
    amount = data.get("amount")

    customer = get_object_or_404(Customer, username=username)
    customer.wallet_balance += amount
    customer.save()

    return JsonResponse({"message": "Wallet charged successfully", "new_balance": str(customer.wallet_balance)})

@csrf_exempt
@require_POST
def deduct_money(request):
    data = json.loads(request.body)
    username = data.get("username")
    amount = data.get("amount")

    customer = get_object_or_404(Customer, username=username)
    if customer.wallet_balance >= amount:
        customer.wallet_balance -= amount
        customer.save()
        return JsonResponse({"message": "Money deducted successfully", "new_balance": str(customer.wallet_balance)})
    else:
        return JsonResponse({"error": "Insufficient funds"}, status=400)

@require_GET
def get_all_customers(request):
    customers = Customer.objects.all()
    customer_list = [{"id": c.id, "full_name": c.full_name, "username": c.username} for c in customers]
    return JsonResponse({"customers": customer_list})

@require_GET
def get_customer_by_username(request, username):
    customer = get_object_or_404(Customer, username=username)
    return JsonResponse({
        "id": customer.id,
        "full_name": customer.full_name,
        "age": customer.age,
        "address": customer.address,
        "gender": customer.gender,
        "marital_status": customer.marital_status,
        "wallet_balance": str(customer.wallet_balance),
    })

