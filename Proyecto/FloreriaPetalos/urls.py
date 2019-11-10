from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',index, name='Inicio'),
    path('catalogo/', catalogo, name='Catalogo'),
    path('login/', login, name='Login'),
    path('registro/', registro, name='Registro'),
    path('registro_producto/', registro_producto, name='Formulario'),
]
