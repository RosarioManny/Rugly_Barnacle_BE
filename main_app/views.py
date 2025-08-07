from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *

# Database Home view
class Home(APIView):
  def get(self, request):
    content = {'Rugly Barncale: Welcome to the Rugly Barnacle Database!'}
    return Response(content)

class ProductList(generics.ListCreateAPIView):
  # Shows a list of all available products
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
  # TODO: Create a method for filtering
# TODO: Create ProductDetails 
class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
  # Show the details of the specified single product
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'id'
# TODO: Create Cart 
# TODO: Create CartDetails 
# TODO: Create CustomOrder 
# TODO: Create Category 
# TODO: Create ProductList 