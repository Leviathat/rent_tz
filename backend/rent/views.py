from rest_framework import generics
from rent.models import Rent, Product, RentProduct
from rent.serializers import RentSerializer, ProductSerializer, RentProductSerializer


class RentAPIView(generics.ListCreateAPIView):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer


class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RentProductAPIView(generics.ListCreateAPIView):
    queryset = RentProduct.objects.all()
    serializer_class = RentProductSerializer
