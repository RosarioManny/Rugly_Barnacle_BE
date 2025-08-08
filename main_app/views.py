from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status 
from .models import *
from .serializers import *

# Database Home view
class Home(APIView):
  def get(self, request):
    content = {'Rugly Barncale: Welcome to the Rugly Barnacle Database!'}
    return Response(content)

# ------------------------------------------------------ PRODUCT ------------------------------------------------------

class ProductList(generics.ListCreateAPIView):
  # Shows a list of all available products
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
  # TODO: Create a method for filtering

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
  # Show the details of the specified single product
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'id'

# ------------------------------------------------------ CART ------------------------------------------------------

class CartView(generics.RetrieveAPIView):
  serializer_class = CartSerializer

  def get_object(self):

    session_key = self.request.session.session_key
    # Get or create a session for the cart.

    if not session_key:
      self.request.session.save() # Create a session.
      session_key = self.request.session.session_key
    
    
    cart, created = Cart.objects.get_or_create(session_key=session_key)
    # Create a Cart. Setting it's session_key to the currant one created.
  
    return cart
  
class AddtoCartView(generics.CreateAPIView):

  def perform_create(self, serializer):
    session_key = self.request.session.session_key

    if not session_key:
      self.request.session.save()
      session_key = self.request.session.session_key

    cart, _ = Cart.objects.get_or_create(session_key=session_key)

    product_id = self.request.data.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    
    # Save the cart item
    serializer.save(cart=cart, product=product)

  
class CartItemDetailView(APIView):
  queryset = CartItem.objects.all()
  serializer_class = ItemSerializer

# TODO: Create CartDetails 

class CustomOrderView(generics.ListCreateAPIView):
  queryset = CustomOrder.objects.all()
  serializer_class = CustomOrderSerializer

  # Create the custom Order
  def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception = True)
    self.perform_create(serializer)

    # TODO:: NOT YET MADE - Send notification funtion
    # send_order_notification(serializer.data)
    print(serializer.data)

    headers = self.get_success_headers(serializer.data)
    return Response(
      serializer.data,
      status= status.HTTP_201_CREATED,
      headers=headers
      )
  # Grab session
  # Grab email
  # Create
# TODO: Create Category 
"""

NOTES:: 
  < CARTVIEW > 
  get_or_create() returns a tuple (object, created) where:
    - object = is the retrieved or created instance
    - created = is a boolean indicating whether a new object was created

"""