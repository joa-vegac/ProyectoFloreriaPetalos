from django.shortcuts import render, redirect
from .models import Estado, Producto, Categoria
from .forms import customuserform, ProductoForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required

from rest_framework import viewsets
from .serializers import ProductoSerializer

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
import json
from fcm_django.models import FCMDevice 

@csrf_exempt
@require_http_methods(['POST'])
def guardar_token(request):
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)

    token = bodyDict['token']

    existe = FCMDevice.objects.filter(registration_id = token, active=True)

    if len(existe) > 0:
        return HttpResponseBadRequest(json.dumps({'mensaje':'El token ya existe.'}))
    
    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True

    if request.user.is_authenticated:
        dispositivo.user = request.user

    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'mensaje':'Token guardado.'}))
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'No se ha podido guardar.'}))

######################################

def index(request):
    productos = Producto.objects.all()
    estados = Estado.objects.all()
    data = {
        'productos':productos,
        'estados': estados
    }
    return render(request, 'core/index.html', data)


def register(request):
    data = {
        'form':customuserform()
    }
    if request.method == 'POST':
        formulario = customuserform(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to="Inicio")
    return render(request, 'registration/register.html', data)


@login_required
def catalogo(request):
    productos=Producto.objects.all()
    return render(request, 'core/catalogo.html',{'productos': productos})

@permission_required('FloreriaPetalos/add_producto')
def registro_producto(request):

    data = {
        'form':ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            dispositivos = FCMDevice.objects.filter(active=True)
            dispositivos.send_message(
                title = "Producto agregado",
                body = "Se ha agregado: " + formulario.cleaned_data['nombre'],
                icon= "static/img/logo.png"
            )
            data['msg'] = "Producto registrado correctamente."
    return render(request,'core/registro_producto.html', data)
    
@permission_required('FloreriaPetalos/add_producto')
def listado_productos(request):
    estados = Estado.objects.all()
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()

    data = {
        'productos':productos,
        'estados': estados,
        'categorias':categorias
    }

    return render(request, 'core/listado_productos.html',data)

@permission_required('FloreriaPetalos/add_producto')
def eliminar_producto(request, id):
    product = Producto.objects.get(id = id)
    product.delete()

    return redirect(to="ListadoProductos")

@permission_required('FloreriaPetalos/add_producto')
def modificar_producto(request, id):
    product = Producto.objects.get(id = id)
    data= {
        'form': ProductoForm(instance=product)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=product, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['msg'] = "Producto modificado correctamente"
            data['form'] = formulario

    return render(request, 'core/modificar_producto.html', data)


@login_required
def informacion(request):
    return render(request, 'core/Info.html')

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer