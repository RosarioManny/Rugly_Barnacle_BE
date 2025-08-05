from rest_framework import serializers
from .models import Product, CartItem, Cart, CustomOrder, Category

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'