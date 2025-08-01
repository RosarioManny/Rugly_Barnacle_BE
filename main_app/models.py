from django.db import models

# Create your models here.

class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(decimal_places=2, max_digits=10)
  category = models.CharField(max_length=24)
  description = models.TextField
  dimensions = models.CharField()
  quantity = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  # Change the name of the display on admin panel
  def __str__(self):
    return self.name
  
# TODO:: Create Cart Model
class Cart(models.Model):
  session_key = models.CharField(max_length=48, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

# TODO:: Create CartItem Model
class CartItem(models.Model):
  cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
  product = models.ForeignKey(Product )
# TODO:: Create CustomOrder Model
# TODO:: Create Session Model
# TODO:: Create Category Model

"""
"""