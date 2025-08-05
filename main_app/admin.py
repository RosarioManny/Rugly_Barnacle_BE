from django.contrib import admin 
from .models import Product, CartItem, Cart, CustomOrder, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(CustomOrder)
admin.site.register(Category)