from django.db import models
from django.utils.text import slugify
from django.db.models import Sum

class Produit(models.Model):
    CATEGORIE_CHOICES = [
        ('pc', 'PC'),
        ('pc_portable', 'PC Portable'),
        ('gaming', 'Gaming'),
        ('telephone', 'Téléphone'),
        ('tablettes', 'Tablettes'),
        ('accessoires', 'Accessoires'),
    ]
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.IntegerField(default=0)
    categorie = models.CharField(max_length=100, choices=CATEGORIE_CHOICES)
    en_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

    def get_slug(self):
        return slugify(self.nom)

    def get_images(self):
        return [image.image.url for image in self.images.all()]

    class Meta:
        db_table = 'web_produit'

class ImageProduit(models.Model):
    produit = models.ForeignKey(Produit, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='produits_images/')

    def __str__(self):
        return f"Image pour {self.produit.nom}"

    class Meta:
        db_table = 'web_imageproduit'


class ContactMessage(models.Model):
    nom = models.CharField(max_length=100)
    sujet = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message de {self.nom} - {self.sujet}"

from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_number_produits(self):
        return self.cartitem_set.aggregate(total=Sum('quantityProducts'))['total'] or 0


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    quantityProducts = models.IntegerField(default=1)