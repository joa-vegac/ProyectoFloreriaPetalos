from django.db import models

class Estado(models.Model):
    nombre_estado=models.CharField(max_length=45)
    def __str__(self):
        return self.nombre_estado

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    valor = models.IntegerField(default=1000)
    descripcion = models.TextField()
    stock = models.IntegerField(default=1)
    imagen= models.ImageField(upload_to='productos')
    estado =models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
