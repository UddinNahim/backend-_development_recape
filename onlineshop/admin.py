from django.contrib import admin
from .models import Product, Category, Order

# admin.site.register(Category)
# The commented out code block `@admin.register(Category)` is a decorator used in Django to register a
# model with the admin site. In this case, it is registering the `Category` model with the admin site
# and providing a custom admin class `CategoryAdmin` that extends `admin.ModelAdmin`.

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['category_name', 'description', 'created_at', 'updated_at']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'price', 'created_at','updated_at']
    search_fields = ['product_name']
    list_filter = ['category']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name','customer_email', 'product', 'quantity', 'created_at','updated_at']

@admin.register(Category)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
       'id', 'category_name','description','created_at','updated_at'
    ]