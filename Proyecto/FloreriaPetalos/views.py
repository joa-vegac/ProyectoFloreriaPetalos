from django.shortcuts import render, redirect
from .models import Estado, Producto
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login as auth_login

def login(request):
    return render(request, 'core/login.html')

def cerrar_sesion(request):
    logout(request)
    return render(request, "core/login.html")

def login_acceso(request):
    if request.POST:
        usuario = request.POST.get("Username")
        contrasena = request.POST.get("Password")

        us = authenticate(request, username=usuario, password=contrasena)
        if us is not None and us.is_active:
            auth_login(request, us)
            return render(request, "core/index.html")
    return render(request, "core/login.html")
    
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            user = form.save()

            if user is not None:
                auth_login(request, user)
                return render(request, "core/index.html")
    return render(request, 'core/register.html')

@login_required(login_url='/login/')
def index(request):
    return render(request, 'core/index.html')

@login_required(login_url='/login/')
def catalogo(request):
    productos=Producto.objects.all()
    return render(request, 'core/catalogo.html',{'productos': productos})

@login_required(login_url='/login/')
def registro_producto(request):
    estados = Estado.objects.all()

    variables = {
        'estados': estados
    }

    if request.POST:
        product = Producto()
        product.nombre = request.POST.get("name")
        product.valor = request.POST.get("value")
        product.descripcion = request.POST.get("desc")
        product.stock = request.POST.get("stock")
        product.imagen = request.FILES.get("image")
        estado = Estado()
        estado.id = request.POST.get("cboestados")
        product.estado = estado

        try:
            product.save()
            variables['msg'] = 'Producto registrado correctamente'
        except:
            variables['msg'] = 'No se pudo registrar el producto'
    
        return render(request, 'core/registro_producto.html', variables)
    return render(request,'core/registro_producto.html', variables)
    

@login_required(login_url='/login/')
def listado_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request, 'core/listado_productos.html', data)
    
@login_required(login_url='/login/')
def eliminar_producto(request, id):
    product = Producto.objects.get(id = id)
    product.delete()

    return redirect(to="ListadoProductos")

@login_required(login_url='/login/')
def modificar_producto(request, id):
    product = Producto.objects.get(id = id)
    estados=Estado.objects.all()

    variables = {
        'estados':estados,
        'producto':product
    }

    if request.POST:
        product = Producto()
        product.id = request.POST.get("txtid")
        product.nombre = request.POST.get("name")
        product.valor = request.POST.get("value")
        product.descripcion = request.POST.get("desc")
        product.stock = request.POST.get("stock")
        product.imagen = request.FILES.get("image")
        estado = Estado()
        estado.id = request.POST.get("cboestados")
        product.estado = estado

        try:
            product.save()
            variables['msg'] = 'Producto modificado correctamente'
        except:
            variables['msg'] = 'No se pudo modificar el producto'

    return render(request, 'core/modificar_producto.html', variables)