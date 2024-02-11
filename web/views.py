from django.shortcuts import render
from .models import Produit

def home(request):
    return render(request, 'home.html')


def produits(request):
    produits = Produit.objects.filter(en_stock=True)
    return render(request, 'products.html', {'produits': produits})