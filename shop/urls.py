from django.conf.urls.static import static
from shop.apps import ShopConfig
from shop.views import ProductsListView, ProductsCreateView, ProductsDetailView, ProductsUpdateView, ProductsDeleteView
from django.urls import path
from django.conf import settings

app_name = ShopConfig.name


urlpatterns = [
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/create/', ProductsCreateView.as_view(), name='products_create'),
    path('products/view/<int:pk>', ProductsDetailView.as_view(), name='products_view'),
    path('products/update/<int:pk>', ProductsUpdateView.as_view(), name='products_update'),
    path('products/delete/<int:pk>', ProductsDeleteView.as_view(), name='products_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
