from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from catalog.models import Product


class HomeView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductsView(ListView):
    model = Product
    template_name = 'catalog/products.html'
