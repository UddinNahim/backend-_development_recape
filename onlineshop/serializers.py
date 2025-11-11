from rest_framework import serializers
from .models import Order  , Product

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class  ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.category_name',read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

