from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from catalog.views import HomeView, ProductsView, ContactsView


urlpatterns = [
    path('', HomeView.as_view()),
    path('contacts/', ContactsView.as_view()),
    path('products/', ProductsView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
