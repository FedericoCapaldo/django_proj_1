from products.api_views import ProductList3
from django.urls import path


urlpatterns = [
  path('api/v1/products', ProductList3)
]
