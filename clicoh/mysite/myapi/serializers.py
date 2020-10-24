from rest_framework import serializers
from .models import Product, Order, OrderDetail

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'date_time')

class OrderDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ('order', 'cuantity', 'price', 'product')