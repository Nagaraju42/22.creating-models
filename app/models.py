from django.db import models

# Create your models here.

class capital(models.Model):
    capital_name=models.CharField(models,primary_key=True)

class Country(models.Model):
    capital_name=models.