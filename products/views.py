from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def products(request):
    """ A view to show the product, including sorting and searching """
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request,'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show an individual product with its details """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request,'products/product_detail.html', context)