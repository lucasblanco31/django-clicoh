from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin)

from .serializers import ProductSerializer, OrderSerializer, OrderDetailSerializer
from .models import Product, Order, OrderDetail

class ProductViewSet(GenericViewSet,    
                    CreateModelMixin, 
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(GenericViewSet,    
                    CreateModelMixin, 
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    ListModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailViewSet(GenericViewSet,    
                    CreateModelMixin, 
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    ListModelMixin):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

# Create your views here.
