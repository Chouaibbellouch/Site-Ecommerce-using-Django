"""
URL configuration for WebsiteEcomm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', views.show_products, name='show_products'),
    path('a-propos/', views.about, name="about"),
    path('contact/',  views.contact, name="contact"),
    path('success/',  views.success, name="success"),
    path('categories/<str:nom_categorie>/', views.categorie, name='categorie'),
    path('recherche/', views.recherche, name='recherche'),
    path('products/<slug:nom_du_produit>/', views.detail_produit, name='detail_produit'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('incrementer_quantity/<int:product_id>/', views.incrementer_quantity, name='incrementer_quantity'),
    path('decrementer_quantity/<int:product_id>/', views.decrementer_quantity, name='decrementer_quantity'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/item_count/', views.cart_item_count, name='cart_item_count'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

