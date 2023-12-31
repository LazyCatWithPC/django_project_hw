from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from catalog.models import Product, Blog


class HomeView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductsView(ListView):
    model = Product
    template_name = 'catalog/products.html'


class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'content', 'image', 'creation_at',)
    template_name = 'catalog/blog_form.html'
    success_url = reverse_lazy('catalog:blogs')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('name', 'content', 'image', 'creation_at',)
    template_name = 'catalog/blog_update.html'

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.name)
            new_blog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog_view', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog
    template_name = 'catalog/blog_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'catalog/blog_view.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blogs')
