from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from api.models import *


def get_categories(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def get_category_by_id(request, id):
    category = Category.objects.get(id=id)
    category_json = category.to_json()
    return JsonResponse(category_json, safe=False)


def get_products(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def get_products_by_id(request, id):
    products = Product.objects.get(id=id)
    products_json = products.to_json()
    return JsonResponse(products_json, safe=False)


def get_products_by_category(request, id):
    get_category_by_id(request, id)
    products = Product.objects.filter(category_id=id)
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)
