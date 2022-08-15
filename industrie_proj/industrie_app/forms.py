from django import forms
from .models import Client, Confiserie, Point_de_vente, Produit, Matière_première, Fournisseur, Fabricant, Confiserie, Magasin
from django.forms import ModelForm



class LoginForm(forms.Form):
    username = forms.CharField(max_length=63,widget=forms.TextInput,  label='Votre nom')
    gmail = forms.CharField(max_length=63,widget=forms.TextInput,  label='Votre adresse mail')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Votre mot de passe')    


class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = ( 'nom', 'conditionnement', 'quantite', )

        labels = {
            'nom': 'Nom',  
            'conditionnement': 'Conditionnement',    
            'quantite': 'Quantite',  
             }

class Matière_premièreForm(ModelForm):
    class Meta:
        model = Matière_première
        fields = ( 'nom', 'quantite', )
        
        labels = {
            'nom': 'Nom',  
            'quantite': 'Quantite',      
            }   

class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = ( 'nom', 'prenom', 'adresse', 'telephone', )

        labels = {
            'nom': 'Nom',  
            'prenom': 'Prenom',    
            'adresse': 'Adresse', 
            'telephone': 'Telephone', 
             } 

class FabricantForm(ModelForm):
    class Meta:
        model = Fabricant
        fields = ( 'confiserie', 'nom', 'prenom', 'adresse', 'telephone', )

        labels = {
            'nom': 'Nom',  
            'prenom': 'Prenom',    
            'adresse': 'Adresse', 
            'telephone': 'Telephone', 
             }

class ConfiserieForm(ModelForm):
    class Meta:
        model = Confiserie
        fields = ( 'nom', 'adresse', )

        labels = {
            'nom': 'Nom',      
            'adresse': 'Adresse', 
             } 

class MagasinForm(ModelForm):
    class Meta:
        model = Magasin
        fields = ( 'nom', 'adresse', 'nombre_magasin', )

        labels = {
            'nom': 'Nom',      
            'adresse': 'Adresse', 
            'nombre_magasin': 'Nombre_magasin', 
             }  

class Point_de_venteForm(ModelForm):
    class Meta:
        model = Point_de_vente
        fields = ( 'nom', 'adresse', 'nombre_point_de_vente', )

        labels = {
            'nom': 'Nom',      
            'adresse': 'Adresse', 
            'nombre_point_de_vente': 'Nombre_point_de_vente', 
             } 

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ( 'nom', 'prenom', 'adresse', 'telephone', )

        labels = {
            'nom': 'Nom',  
            'prenom': 'Prenom',    
            'adresse': 'Adresse', 
            'telephone': 'Telephone', 
             }                                                                                  
