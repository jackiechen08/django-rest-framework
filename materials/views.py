from rest_framework import generics
from materials.models import Polymer, Producer, Product
from materials.serializers import PolymerSerializer, ProducerSerializer, ProductSerializer

class PolymerList(generics.ListCreateAPIView):
    queryset = Polymer.objects.all()
    serializer_class = PolymerSerializer

class PolymerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Polymer.objects.all()
    serializer_class = PolymerSerializer

class ProducerList(generics.ListCreateAPIView):   
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

class ProducerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

class ProductList(generics.ListCreateAPIView):   
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer