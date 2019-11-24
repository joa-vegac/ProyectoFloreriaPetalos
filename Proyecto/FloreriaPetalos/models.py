from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)
    valor = models.IntegerField(default=1000)
    descripcion = models.TextField()
    stock = models.IntegerField(default=1)
    imagen= models.ImageField(upload_to='productos', null=True)

    def __str__(self):
        return self.nombre
