from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre_categoria=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_categoria

class Estado(models.Model):
    nombre_estado=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre_estado

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.IntegerField(default=1000)
    descripcion = models.TextField(null=True, blank=True)
    stock = models.IntegerField(default=1)
    imagen= models.ImageField(upload_to='productos')
    estado =models.ForeignKey(Estado, on_delete=models.CASCADE)
    categoria =models.ForeignKey(Categoria, on_delete=models.CASCADE)

    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nombre


