from django.db import models

# Create your models here.

class Pizza(models.Model):
    nom = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    prix =models.FloatField(max_length=0)
    vegetarienne = models.BooleanField(False)
    nombre = models.IntegerField()


    def __str__(self) -> str:
        return self.nom