from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index, name='Inicio'),
    path('catalogo/', catalogo, name='Catalogo'),
    path('registro_producto/', registro_producto, name='Formulario'),
    path('register/', register, name='Register'),
    path('listado_productos/', listado_productos, name='ListadoProductos'),
    path('eliminar_producto/<id>/', eliminar_producto, name='EliminarProducto'),
    path('modificar_producto/<id>/', modificar_producto, name='ModificarProducto'),
]