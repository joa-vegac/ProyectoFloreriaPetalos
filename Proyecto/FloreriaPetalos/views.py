from django.shortcuts import render, redirect
from .models import Estado, Producto
from .forms import customuserform, ProductoForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    estados = Estado.objects.all()
    productos = Producto.objects.all()

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
    
@permission_required('FloreriaPetalos/add_producto')
def listado_productos(request):
    estados = Estado.objects.all()
    productos = Producto.objects.all()

    data = {
        'productos':productos,
        'estados': estados
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
