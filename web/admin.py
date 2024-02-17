from django.contrib import admin
from .models import Produit, ImageProduit

class ImageProduitAdmin(admin.StackedInline):
    model = ImageProduit
    extra = 1  # Nombre d'images à afficher par défaut

class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom', 'categorie']
    inlines = [ImageProduitAdmin]

admin.site.register(Produit, ProduitAdmin)
admin.site.register(ImageProduit)


