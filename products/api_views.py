from rest_framework.generics import ListAPIView

from products.serializers import GenericProductSerializer
from products.data_layer.product_data_layer import get_products


class ProductList3(ListAPIView):
    queryset = get_products()
    serializer_class = GenericProductSerializer
