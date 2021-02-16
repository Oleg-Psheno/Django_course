from django.shortcuts import render
from mainapp.models import Product, ProductCategory

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')
# коментарий для того чтобы новая ветвь отличалась от master

def products(request, category_id=None):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    context = {
            'categories': ProductCategory.objects.all(),
            'products': products
        }
    return render(request, 'mainapp/products.html', context)