from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.IntegerField(default=0)
    en_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = 'web_produit'

class ImageProduit(models.Model):
    produit = models.ForeignKey(Produit, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='produits_images/')

    def __str__(self):
        return f"Image pour {self.produit.nom}"

    class Meta:
        db_table = 'web_imageproduit'
