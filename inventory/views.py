# inventory/views.py

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST,require_http_methods, require_GET
import json

from .models import Good

@csrf_exempt
@require_POST
def add_good(request):
    data = json.loads(request.body)
    try:
        good = Good.objects.create(**data)
        return JsonResponse({"message": "Good added successfully", "id": good.id})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def deduct_good(request, good_id):
    good = get_object_or_404(Good, id=good_id)
    good.count_in_stock -= 1
    good.save()
    return JsonResponse({"message": "Good deducted successfully", "new_count_in_stock": good.count_in_stock})

@csrf_exempt
@require_http_methods(["PUT"])
def update_good(request, good_id):
    data = json.loads(request.body)
    try:
        good = Good.objects.get(id=good_id)
        for key, value in data.items():
            setattr(good, key, value)
        good.save()
        return JsonResponse({"message": "Good updated successfully"})
    except Good.DoesNotExist:
        return JsonResponse({"error": "Good not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@require_GET
def get_all_goods(request):
    goods = Good.objects.all()
    goods_list = [{"id": g.id, "name": g.name, "category": g.category, "price_per_item": str(g.price_per_item), "count_in_stock": g.count_in_stock} for g in goods]
    return JsonResponse({"goods": goods_list})

@require_GET
def get_good_by_id(request, good_id):
    good = get_object_or_404(Good, id=good_id)
    return JsonResponse({
        "id": good.id,
        "name": good.name,
        "category": good.category,
        "price_per_item": str(good.price_per_item),
        "description": good.description,
        "count_in_stock": good.count_in_stock,
    })

