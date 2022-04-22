from django.shortcuts import render#permet d'aller chercher un template et donner son rendu
from django.http import HttpResponse
from .models import Pizza
# Create your views here.
#exercice
#Les Pizzas: Végétarienne: 8.5€,Poulet champignons: 8.5€,4 fromages: 8.5€,Carnivore:8.5€

#1--acceder par /menu
def index(request):
    """pizzas=Pizza.objects.all()#recuperer les objets de notre db collections
    pizzas_names_price =[pizza.nom  + " : " + str(pizza.prix )+ " €"  for pizza in pizzas]
    pizzas_names_price_str=" , ".join(pizzas_names_price)
    return HttpResponse("Les Pizzas: " + pizzas_names_price_str)#retourner du texte"""
    pizzas=Pizza.objects.all()
    return render(request, 'menu/index.html', locals())