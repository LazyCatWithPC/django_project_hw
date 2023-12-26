from django.shortcuts import render
from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')


def products(request):

    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }

    return render(request, 'catalog/products.html', context)
