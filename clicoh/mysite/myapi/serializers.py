from rest_framework import serializers
from .models import Product, Order, OrderDetail

class ProductSerializer(serializers.ModelSerializer):
    
    def validate_price(self):
        if self.price > 5:
            raise serializers.ValidationError("Price must be low than 5.")   
    
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'