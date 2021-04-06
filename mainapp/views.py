from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_page

@cache_page(10)
def index(request):
    context = {'title':'Главная'}
    return render(request, 'mainapp/index.html', context)


# def products(request, category_id=None):
#     products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#     context = {
#             'categories': ProductCategory.objects.all(),
#             'products': products
#         }
#     return render(request, 'mainapp/products.html', context)

def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id).order_by('price')
    else:
        products = Product.objects.all().order_by('price')
    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page)
    context = {
        'categories': ProductCategory.get_all(),
        'products': products_paginator
    }
    return render(request, 'mainapp/products.html', context)



