from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from catalog.views import HomeView, ProductsView, ContactsView, BlogView, BlogListView, BlogDetailView, BlogUpdateView, \
    BlogDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view()),
    path('contacts/', ContactsView.as_view()),
    path('products/', ProductsView.as_view()),
    path('blogs/create/', BlogView.as_view(), name='blog_create'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blogs/view/<int:pk>', BlogDetailView.as_view(), name='blog_view'),
    path('blogs/update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
