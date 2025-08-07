from rest_framework import serializers
from .models import Product, CartItem, Cart, CustomOrder, Category

# CATEGORY
class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model = Category
    fields = '__all__'

# PRODUCT
class ProductSerializer(serializers.ModelSerializer):
  
  category = CategorySerializer(read_only=True)

  class Meta:
    model = Product
    fields = '__all__'

# CART
class CartSerializer(serializers.ModelSerializer):

  class Meta:
    model = Cart
    fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):

  class Meta:
    model = CartItem
    fields = '__all__'