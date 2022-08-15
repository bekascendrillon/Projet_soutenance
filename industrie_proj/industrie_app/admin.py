from django.contrib import admin

# Register your models here.
from .models import Confiserie, Produit, Matière_première, Fournisseur, Magasin, Point_de_vente, Client, Fabricant  


admin.site.register(Confiserie)
admin.site.register(Produit)
admin.site.register(Matière_première)
admin.site.register(Fournisseur)
admin.site.register(Magasin)
admin.site.register(Point_de_vente)
admin.site.register(Client)
admin.site.register(Fabricant)