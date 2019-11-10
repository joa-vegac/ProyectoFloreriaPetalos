from django.db import models

# Create your models here.

class User (models.Model):
    email =  models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Producto (models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    valor = models.IntegerField()
    desc = models.TextField(max_length=400)
    estado = models.CharField(max_length=15)
    stock = models.IntegerField()