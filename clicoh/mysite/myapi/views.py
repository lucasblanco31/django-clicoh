from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer, OrderSerializer, OrderDetailSerializer
from .models import Product, Order, OrderDetail
from django.shortcuts import get_object_or_404

class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    def list(self, request):
        productos = Product.objects.all()
        serializer = ProductSerializer(productos, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        producto = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(producto)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk=None):
        queryset = Product.objects.all()
        producto = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        queryset = Product.objects.all()
        producto = get_object_or_404(queryset, pk=pk)
        producto.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

class OrderDetailViewSet(viewsets.ModelViewSet):

    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()

    def list(self, request):
        orders = OrderDetail.objects.all()
        serializer = OrderDetailSerializer(orders, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = OrderDetail.objects.all()
        orders = get_object_or_404(queryset, pk=pk)
        serializer = OrderDetailSerializer(orders)
        return Response(serializer.data)
        
    def create(self, request):
        serializer = OrderDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk=None):
        queryset = OrderDetail.objects.all()
        orders = get_object_or_404(queryset, pk=pk)
        serializer = OrderDetailSerializer(orders, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        queryset = OrderDetail.objects.all()
        orders = get_object_or_404(queryset, pk=pk)
        orders.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

class OrderViewSet(viewsets.ModelViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def list(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def create(self, request):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        order.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)