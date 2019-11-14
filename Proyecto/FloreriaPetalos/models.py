from django.db import models

# Create your models here.

class Producto (models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    valor = models.IntegerField()
    desc = models.TextField(max_length=400)
    image = models.ImageField(upload_to='producto',null=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

