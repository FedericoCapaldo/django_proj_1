from products.models import Product

def get_products():
    all_prods = list(Product.objects.values())
    return all_prods