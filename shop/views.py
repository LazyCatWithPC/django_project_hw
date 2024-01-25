from django.forms import inlineformset_factory
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from shop.forms import ProductForm, VersionForm
from shop.models import Product, Version
from django.urls import reverse_lazy


class ProductsListView(ListView):
    model = Product
    template_name = 'shop/products.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        for product in context['object_list']:
            active_version = product.version_set.filter(is_active=True).first()
            if active_version:
                product.active_version_number = active_version.number
                product.active_version_name = active_version.name
            else:
                product.active_version_number = None
                product.active_version_name = None

        return context


class ProductsCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shop:products')


class ProductsUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shop:products')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            
        return super().form_valid(form)


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'shop/products_view.html'


class ProductsDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shop:products')
