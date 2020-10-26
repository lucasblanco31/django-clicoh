from rest_framework import serializers
from .models import Product, Order, OrderDetail

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    #product = ProductSerializer(many=True, read_only=False)
    class Meta:
        model = OrderDetail
        fields = '__all__'
