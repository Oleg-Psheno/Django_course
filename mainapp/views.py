from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')
# коментарий для того чтобы новая ветвь отличалась от master

def products(request):
    return render(request, 'mainapp/products.html')