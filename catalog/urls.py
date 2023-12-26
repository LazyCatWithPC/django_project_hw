from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from catalog.views import home, products
from catalog.views import contacts

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('products/', products),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
