from django.urls import path
from .views import *

urlpatterns = [
  path('', Home.as_view(), name='home'),
  # TODO* :: Create products/ route
  path('products/', ProductList.as_view(), name='product-list'),
  # TODO :: Create products/<int:product_id> route
  path('products/<int:id>', ProductDetails.as_view(), name='product-details')
  # TODO :: Create cart/ route
  # TODO :: Create cart/items route
  # TODO :: Create cart/items/<int:item_id> route
  # TODO :: Create categories/ route
  # TODO :: Create custom/ route
]