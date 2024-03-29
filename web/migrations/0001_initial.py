# Generated by Django 5.0.1 on 2024-02-11 01:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantite', models.IntegerField(default=0)),
                ('en_stock', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='produits_images/')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='web.produit')),
            ],
        ),
    ]
