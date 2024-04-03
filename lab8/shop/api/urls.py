from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('products/', get_products),
    path('products/<int:id>/', get_products_by_id),
    path('categories/', get_categories),
    path('categories/<int:id>/', get_category_by_id),
    path('categories/<int:id>/products', get_products_by_category),
]
