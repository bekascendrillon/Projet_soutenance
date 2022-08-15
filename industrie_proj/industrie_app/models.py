from aiohttp import request
from django.db import models

# Create your models here.


class Image(models.Model):
    caption=models.CharField(max_length=50)
    image=models.ImageField(upload_to="img/%y")
    def __str__(self):
        return self.caption


class Confiserie(models.Model):
    nom = models.CharField('Nom', max_length=120)
    adresse = models.CharField('Adresse', max_length=120)

class Produit(models.Model):
    nom = models.CharField('Nom', max_length=100)
    conditionnement = models.CharField('Conditionnement', max_length=100)
    quantite= models.CharField('Quantite', max_length=100)

class Matière_première (models.Model):
    nom = models.CharField('Nom', max_length=120)
    quantite = models.CharField('Quantite', max_length=100)
								
class Fournisseur(models.Model):
    nom = models.CharField('Nom', max_length=120)
    prenom = models.CharField('Prenom', max_length=120)
    adresse = models.CharField('Adresse', max_length=120)
    telephone = models.CharField('Telephone', max_length=50)
								
class Magasin(models.Model):
    nom = models.CharField('Nom', max_length=120)
    adresse = models.CharField('Adresse', max_length=120)
    nombre_magasin = models.CharField('Nombre_magasin', max_length=120)
								
class Point_de_vente(models.Model):
    nom = models.CharField('Nom', max_length=120)
    adresse = models.CharField('Adresse', max_length=120)
    nombre_point_de_vente = models.CharField('Nombre_point_de_vente', max_length=120)
								
class Client(models.Model):
    nom = models.CharField('Nom', max_length=120)
    prenom = models.CharField('Prenom', max_length=120)
    adresse = models.CharField('Adresse', max_length=120)
    telephone = models.CharField('Telephone', max_length=50)	

class Fabricant(models.Model):
    confiserie = models.ForeignKey(Confiserie, blank=False, null=False, on_delete=models.CASCADE)
    nom = models.CharField('Nom', max_length=120)
    prenom = models.CharField('Prenom', max_length=120)
    adresse = models.CharField('Adresse', max_length=120)
    telephone = models.CharField('Telephone', max_length=50)
								
def __str__(self):
    return self.confiserie
