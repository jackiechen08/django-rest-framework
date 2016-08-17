from rest_framework import generics, renderers, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from materials.models import Polymer, Producer, Product
from materials.serializers import PolymerSerializer, ProducerSerializer, ProductSerializer, UserSerializer
from materials.permissions import IsOwnerOrReadOnly

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'polymers': reverse('polymer-list', request=request, format=format),
        'producers':reverse('producer-list', request=request, format = format),
        'products': reverse('product-list', request = request, format = format)
    })
#user-list, polymer-list.... are in the materials/urls.py

class PolymerList(generics.ListCreateAPIView):
    queryset = Polymer.objects.all()
    serializer_class = PolymerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    #The create() method of our serializer will now be passed an additional 'owner' field, along with the validated data from the request.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PolymerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Polymer.objects.all()
    serializer_class = PolymerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


class ProducerList(generics.ListCreateAPIView):   
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProducerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


class ProductList(generics.ListCreateAPIView):   
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer