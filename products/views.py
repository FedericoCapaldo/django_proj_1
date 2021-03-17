from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.serializers import ProductSerializer
from products.models import Product


class ProductList2(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
