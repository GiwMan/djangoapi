from dataclasses import field, fields
from rest_framework import serializers

from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
    # title = serializers.CharField(max_length=120)
    # content = serializers.CharField(max_length=100)
    # price = serializers.DecimalField(max_digits=15,decimal_places=2, default=99.99)