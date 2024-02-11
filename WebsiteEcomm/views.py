from django.shortcuts import render
from web.models import Produit

def home(request):
    return render(request, 'home.html')



def show_products(request):
    produits = Produit.objects.all()  # Récupérer tous les produits
    return render(request, 'products.html', {'produits': produits})
