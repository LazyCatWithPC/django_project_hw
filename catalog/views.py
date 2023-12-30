from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView

from catalog.models import Product, Blog


class HomeView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductsView(ListView):
    model = Product
    template_name = 'catalog/products.html'


class BlogView(CreateView):
    model = Blog
    fields = ('name', 'content', 'image', 'creation_at',)
    template_name = 'catalog/blog_form.html'
    success_url = reverse_lazy('catalog:blogs')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'content', 'image', 'creation_at',)
    template_name = 'catalog/blog_update.html'
    success_url = reverse_lazy('catalog:blogs')


class BlogListView(ListView):
    model = Blog
    template_name = 'catalog/blog_list.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'catalog/blog_view.html'


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blogs')
