from zipfile import ZIP_BZIP2
from django.contrib import admin
from .models import Pizza


#creer une classe pour personnaliser pour admin
class PizzaAdmin(admin.ModelAdmin):
    list_display =('nom', 'ingredients', 'vegetarienne', 'prix','nombre')
    search_fields = ['nom']#option de recherche
# Register your models here.
admin.site.register(Pizza, PizzaAdmin)
