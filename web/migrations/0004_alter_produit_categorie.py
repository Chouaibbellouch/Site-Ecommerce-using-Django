# Generated by Django 5.0.1 on 2024-02-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_produit_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='categorie',
            field=models.CharField(choices=[('pc', 'PC'), ('pc_portable', 'PC Portable'), ('gaming', 'Gaming'), ('telephone', 'Téléphone'), ('tablettes', 'Tablettes'), ('accessoires', 'Accessoires')], max_length=100),
        ),
    ]