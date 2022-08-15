from django.urls import path, include
from . import views

from django.contrib import admin





urlpatterns = [
    path('home', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('', views.login_page, name='login'),
    path('Apropos', views.Apropos, name='Apropos'),
    path('produit_liste', views.produit_liste, name='produit-liste'),
    path('ajout_produit', views.ajout_produit, name='ajout-produit'),
    path('modifier_produit/<produit_id>', views.modifier_produit, name='modifier-produit'),
    path('supprimer_produit/<produit_id>', views.supprimer_produit, name='supprimer-produit'),
    path('matière_première_list', views.matière_première_liste, name='matière_première-liste'),
    path('ajout_matière_première', views.ajout_matière_première, name='ajout-matière_première'),
    path('modifier_matière_première/<matière_première_id>', views.modifier_matière_première, name='modifier-matière_première'),
    path('supprimer_matière_première/<matière_première_id>', views.supprimer_matière_première, name='supprimer-matière_première'),
    path('fournisseur_liste', views.fournisseur_liste, name='fournisseur-liste'),
    path('ajout_fournisseur', views.ajout_fournisseur, name='ajout-fournisseur'),
    path('modifier_fournisseur/<fournisseur_id>', views.modifier_fournisseur, name='modifier-fournisseur'),
    path('supprimer_fournisseur/<fournisseur_id>', views.supprimer_fournisseur, name='supprimer-fournisseur'),
    path('fabricant_liste', views.fabricant_liste, name='fabricant-liste'),
    path('ajout_fabricant', views.ajout_fabricant, name='ajout-fabricant'),
    path('modifier_fabricant/<fabricant_id>', views.modifier_fabricant, name='modifier-fabricant'),
    path('supprimer_fabricant/<fabricant_id>', views.supprimer_fabricant, name='supprimer-fabricant'),
    path('confiserie_liste', views.confiserie_liste, name='confiserie-liste'),
    path('ajout_confiserie', views.ajout_confiserie, name='ajout-confiserie'),
    path('modifier_confiserie/<confiserie_id>', views.modifier_confiserie, name='modifier-confiserie'),
    path('supprimer_confiserie/<confiserie_id>', views.supprimer_confiserie, name='supprimer-confiserie'),
    path('magasin_liste', views.magasin_liste, name='magasin-liste'),
    path('ajout_magasin', views.ajout_magasin, name='ajout-magasin'),
    path('modifier_magasin/<magasin_id>', views.modifier_magasin, name='modifier-magasin'),
    path('supprimer_magasin/<magasin_id>', views.supprimer_magasin, name='supprimer-magasin'),
    path('point_de_vente_liste', views.point_de_vente_liste, name='point_de_vente-liste'),
    path('ajout_point_de_vente', views.ajout_point_de_vente, name='ajout-point_de_vente'),
    path('modifier_point_de_vente/<point_de_vente_id>', views.modifier_point_de_vente, name='modifier-point_de_vente'),
    path('supprimer_point_de_vente/<point_de_vente_id>', views.supprimer_point_de_vente, name='supprimer-point_de_vente'),
    path('client_liste', views.client_liste, name='client-liste'),
    path('ajout_client', views.ajout_client, name='ajout-client'),
    path('modifier_client/<client_id>', views.modifier_client, name='modifier-client'),
    path('supprimer_client/<client_id>', views.supprimer_client, name='supprimer-client'),
    path('details_produit/<produit_id>', views.details_produit, name='details-produit'),
    path('details_matière_première/<matière_première_id>', views.details_matière_première, name='details-matière_première'),
    path('details_fabricant/<fabricant_id>', views.details_fabricant, name='details-fabricant'),
    path('details_confiserie/<confiserie_id>', views.details_confiserie, name='details-confiserie'),
    path('details_fournisseur/<fournisseur_id>', views.details_fournisseur, name='details-fournisseur'),
    path('details_magasin/<magasin_id>', views.details_magasin, name='details-magasin'),
    path('details_point_de_vente/<point_de_vente_id>', views.details_point_de_vente, name='details-point_de_vente'),
    path('details_client/<client_id>', views.details_client, name='details-client'),



]