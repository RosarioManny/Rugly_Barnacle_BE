from django.db import models

# To Create an enums or choice 
PRICES = (
  ('SM', '$150-$249'),
  ('MD', '$250-$349'),
  ('LG', '$350-$449'),
  ('XL', '$450'),
)
# Create your models here.

class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(decimal_places=2, max_digits=10)
  category = models.CharField(max_length=24)
  description = models.TextField()
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
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
# TODO:: Create CustomOrder Model
class CustomOrder(models.Model):
  description = models.CharField
  email = models.CharField
  price = models.CharField(max_length=2, choices=PRICES, default=PRICES[0][0])
  created_at = models.DateTimeField(auto_now_add=True)
# TODO:: Create Session Model
# TODO:: Create Category Model

"""
Make migrations::
> python manage.py makemigrations

>> How does models.ForeignKey Work? << 
1. Creates a Many-to-One relation. Creates a column in the db with the specified relations (Id). This case, Cartitem -> Cart(specifically Cart's Id)
2. Arg1 specifies what the relation is too. Ex: CartItems.cart is related Cart; CartItems.product is related to Product.
3. related_name refers to the inverse from Cart -> CartItem. 
  3a. Without: You'd use cart.cartitem_set.all()
      With: You use cart.items.all() (clearer)
4. on_delete defines what happens on delete. CASCADE refers to how it deletes; Delete all CartItems if their Cart is deleted.
"""