from django.shortcuts import render, redirect 
from .models import Fabricant, Point_de_vente, Produit, Matière_première, Fournisseur, Confiserie, Magasin, Client 
from .forms import ProduitForm, Matière_premièreForm, FournisseurForm, FabricantForm, ConfiserieForm, MagasinForm, Point_de_venteForm, ClientForm
from django.http import HttpResponseRedirect, HttpResponse

from . import forms
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.



def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        gmail = request.POST['gmail']
        password = request.POST['password']
        user = authenticate(username=username, gmail=gmail, password=password)
        if user is not None:
            return redirect('home')
        else:
            return render(request, 'production/login.html')

    return render(request, 'production/login.html')
    

def Apropos(request):
    return render(request, 'production/Apropos.html', {})   

@login_required
def home(request):
    return render(request, 'production/home.html', {})
	
def produit_liste(request):
    produits = Produit.objects.all()
    if request.method == "GET":
        name = request.GET.get('recherche')
        if name is not None:
            produits = Produit.objects.filter(nom__icontains=name)
    return render(request, 'production/produit_liste.html', {
                    'produits': produits,
                    })


def ajout_produit(request):
    submitted = False
    if request.method == "POST":
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ajout_produit?submitted=True')
    else:
        form = ProduitForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'production/ajout_produit.html', {
        'form': form,
        'submitted': submitted,
    })

def modifier_produit(request,produit_id):
    produits = Produit.objects.get(pk=produit_id)
    form = ProduitForm(request.POST or None, instance=produits)
    if form.is_valid():
        form.save()
        return redirect('produit-liste')
    return render(request, 'production/modifier_produit.html', {
        'produits': produits,
        'form': form,
        }) 

def supprimer_produit(request, produit_id):
    produits = Produit.objects.get(pk=produit_id)
    produits.delete()
    return redirect('produit-liste')   



def matière_première_liste(request):
    matière_premières = Matière_première.objects.all()
    if request.method == "GET":
        name = request.GET.get('recherche')
        if name is not None:
            matière_premières = Matière_première.objects.filter(nom__icontains=name)
    return render(request, 'production/matière_première_liste.html', {
                    'matière_premières': matière_premières,
                    }) 

def ajout_matière_première(request):
    submitted = False
    if request.method == "POST":
        form = Matière_premièreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ajout_matière_première?submitted=True')
    else:
        form = Matière_premièreForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'production/ajout_matière_première.html', {
        'form': form,
        'submitted': submitted,
    })  

def modifier_matière_première(request, matière_première_id):
    matière_premières = Matière_première.objects.get(pk=matière_première_id)
    form = Matière_premièreForm(request.POST or None, instance=matière_premières)
    if form.is_valid():
        form.save()
        return redirect('matière_première-liste')
    return render(request, 'production/modifier_matière_première.html', {
            'matière_premières': matière_premières,
            'form': form,
            })

def supprimer_matière_première(request, matière_première_id):
    matière_premières = Matière_première.objects.get(pk=matière_première_id)
    matière_premières.delete()
    return redirect('matière_première-liste')


def fournisseur_liste(request):
    fournisseurs = Fournisseur.objects.all()
    if request.method == "GET":
        name = request.GET.get('recherche')
        if name is not None:
            fournisseurs = Fournisseur.objects.filter(nom__icontains=name)
    return render(request, 'production/fournisseur_liste.html', {
                    'fournisseurs': fournisseurs,
                    })

            

def ajout_fournisseur(request):
    submitted = False
    if request.method == "POST":
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ajout_fournisseur?submitted=True')
    else:
        form = FournisseurForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'production/ajout_fournisseur.html', {
        'form': form,
        'submitted': submitted,
    })

def modifier_fournisseur(request, fournisseur_id):
    fournisseurs = Fournisseur.objects.get(pk=fournisseur_id)
    form = FournisseurForm(request.POST or None, instance=fournisseurs)
    if form.is_valid():
        form.save()
        return redirect('fournisseur-liste')
    return render(request, 'production/modifier_fournisseur.html', {
            'fournisseurs': fournisseurs,
            'form': form,
            })

def supprimer_fournisseur(request, fournisseur_id):
    fournisseurs = Fournisseur.objects.get(pk=fournisseur_id)
    fournisseurs.delete()
    return redirect('fournisseur-liste') 

def fabricant_liste(request):
    fabricants = Fabricant.objects.all()
    if request.method == "GET":
        name = request.GET.get('recherche')
        if name is not None:
            fabricants = Fabricant.objects.filter(nom__icontains=name)
    return render(request, 'production/fabricant_liste.html', {
                    'fabricants': fabricants,
                    })

def ajout_fabricant(request):
    submitted = False
    if request.method == "POST":
        form = FabricantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ajout_fabricant?submitted=True')
    else:
        form = FabricantForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'production/ajout_fabricant.html', {
        'form': form,
        'submitted': submitted,
    })

def modifier_fabricant(request, fabricant_id):
    fabricants = Fabricant.objects.get(pk=fabricant_id)
    form = FabricantForm(request.POST or None, instance=fabricants)
    if form.is_valid():
        form.save()
        return redirect('fabricant-liste')
    return render(request, 'production/modifier_fabricant.html', {
            'fabricants': fabricants,
            'form': form,
            }) 

def supprimer_fabricant(request, fabricant_id):
    fabricants = Fabricant.objects.get(pk=fabricant_id)
    fabricants.delete()
    return redirect('fabricant-liste') 

def confiserie_liste(request):
    confiseries = Confiserie.objects.all()
    if request.method == "GET":
        name = request.GET.get('recherche')
        if name is not None:
            confiseries = Confiserie.objects.filter(nom__icontains=name)
    return render(request, 'production/confiserie_liste.html', {
                    'confiseries': confiseries,
                    }) 

def ajout_confiserie(request):
    submitted = False
    if request.method == "POST":
        form = ConfiserieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ajout_confiserie?submitted=True')
    else:
        form = ConfiserieForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'production/ajout_confiserie.html', {
        'form': form,
        'submitted': submitted,
    }) 

def modifier_confiserie(request, confiserie_id):
    confiseries = Confiserie.objects.get(pk=confiserie_id)
    form = ConfiserieForm(request.POST or None, instance=confiseries)
    if form.is_valid():
        form.save()
        return redirect('confiserie-liste')
    return render(request, 'production/modifier_confiserie.html', {
            'confiseries': confiseries,
            'form': form,
            }) 

def supprimer_confiserie(request, confiserie_id):
    confiseries = Confiserie.objects.get(pk=confiserie_id)
    confiseries.delete()
    return redirect('confiserie-liste') 

def magasin_liste(request):
    magasins = Magasin.objects.all()
    if request.method == "GET":
        name = request.GET.get('recherche')
        if name is not None:
            magasins = Magasin.objects.filter(nom__icontains=name)
    return render(request, 'production/magasin_liste.html', {
                    'magasins': magasins,
                    }) 

def ajout_magasin(request):
    submitted = False
    if request.method == "POST":
        form = MagasinForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ajout_magasin?submitted=True')
    else:
        form = MagasinForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'production/ajout_magasin.html', {
        'form': form,
        'submitted': submitted,
    })

def modifier_magasin(request, magasin_id):
    magasins = Magasin.objects.get(pk=magasin_id)
    form = MagasinForm(request.POST or None, instance=magasins)
    if form.is_valid():
        form.save()
        return redirect('magasin-liste')
    return render(request, 'production/modifier_magasin.html', {
            'magasins': magasins,
            'form': form,
            })

def supprimer_magasin(request, magasin_id):
    magasins = Magasin.objects.get(pk=magasin_id)
    magasins.delete()
    return redirect('magasin-liste') 

def point_de_vente_liste(request):
    point_de_ventes = Point_de_vente.objects.all()
    if request.method == "GET":
        name = request.GET.get('recherche')
        if name is not None:
            point_de_ventes = Point_de_vente.objects.filter(nom__icontains=name)
    return render(request, 'production/point_de_vente_liste.html', {
                    'point_de_ventes': point_de_ventes,
                    })

def ajout_point_de_vente(request):
    submitted = False
    if request.method == "POST":
        form = Point_de_venteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ajout_point_de_vente?submitted=True')
    else:
        form = Point_de_venteForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'production/ajout_point_de_vente.html', {
        'form': form,
        'submitted': submitted,
    })

def modifier_point_de_vente(request, point_de_vente_id):
    point_de_ventes = Point_de_vente.objects.get(pk=point_de_vente_id)
    form = Point_de_venteForm(request.POST or None, instance=point_de_ventes)
    if form.is_valid():
        form.save()
        return redirect('point_de_vente-liste')
    return render(request, 'production/modifier_point_de_vente.html', {
            'point_de_ventes': point_de_ventes,
            'form': form,
            })

def supprimer_point_de_vente(request, point_de_vente_id):
    point_de_ventes = Point_de_vente.objects.get(pk=point_de_vente_id)
    point_de_ventes.delete()
    return redirect('point_de_vente-liste')

def client_liste(request):
    clients = Client.objects.all()
    if request.method == "GET":
        name = request.GET.get('recherche')
        if name is not None:
            clients = Client.objects.filter(nom__icontains=name)
    return render(request, 'production/client_liste.html', {
                    'clients': clients,
                    }) 

def ajout_client(request):
    submitted = False
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ajout_client?submitted=True')
    else:
        form = ClientForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'production/ajout_client.html', {
        'form': form,
        'submitted': submitted,
    })

def modifier_client(request, client_id):
    clients = Client.objects.get(pk=client_id)
    form = ClientForm(request.POST or None, instance=clients)
    if form.is_valid():
        form.save()
        return redirect('client-liste')
    return render(request, 'production/modifier_client.html', {
            'clients': clients,
            'form': form,
            }) 

def supprimer_client(request, client_id):
    clients = Client.objects.get(pk=client_id)
    clients.delete()
    return redirect('client-liste')  

def details_produit(request, produit_id):
    produits = Produit.objects.get(pk=produit_id)
    return render(request, 'production/details_produit.html', {
        'produits': produits,
        }) 

from django.db.models import Q

    

def details_matière_première(request, matière_première_id):
    matière_premières = Matière_première.objects.get(pk=matière_première_id)
    return render(request, 'production/details_matière_première.html', {
        'matière_premières': matière_premières,
        }) 

def details_fabricant(request, fabricant_id):
    fabricants = Fabricant.objects.get(pk=fabricant_id)
    return render(request, 'production/details_fabricant.html', {
        'fabricants': fabricants,
        }) 

def details_confiserie(request, confiserie_id):
    confiseries = Confiserie.objects.get(pk=confiserie_id)
    return render(request, 'production/details_confiserie.html', {
        'confiseries': confiseries,
        }) 

def details_fournisseur(request, fournisseur_id):
    fournisseurs = Fournisseur.objects.get(pk=fournisseur_id)
    return render(request, 'production/details_fournisseur.html', {
        'fournisseurs': fournisseurs,
        }) 

def details_magasin(request, magasin_id):
    magasins = Magasin.objects.get(pk=magasin_id)
    return render(request, 'production/details_magasin.html', {
        'magasins': magasins,
        }) 

def details_point_de_vente(request, point_de_vente_id):
    point_de_ventes = Point_de_vente.objects.get(pk=point_de_vente_id)
    return render(request, 'production/details_point_de_vente.html', {
        'point_de_ventes': point_de_ventes,
        }) 

def details_client(request, client_id):
    clients = Client.objects.get(pk=client_id)
    return render(request, 'production/details_client.html', {
        'clients': clients,
        }) 

        

