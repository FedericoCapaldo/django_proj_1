from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name', 'product_description')
        depth = 1

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
