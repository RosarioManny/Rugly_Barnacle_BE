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

  def __str__(self):
    return self.name
# TODO:: Create Cart Model
# TODO:: Create CartItem Model
# TODO:: Create CustomOrder Model
# TODO:: Create Session Model