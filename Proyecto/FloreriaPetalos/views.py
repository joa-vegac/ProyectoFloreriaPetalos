from django.shortcuts import render, redirect
from .models import Estado, Producto
from .forms import customuserform, ProductoForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required

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

def index(request):
    return render(request, 'core/index.html')

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
    stock = 0

    data = {
        'productos':productos,
        'estados': estados
    }

    if request.POST.get('stock'):
        stock = int(request.POST.get('stock'))
        productos = productos.filter(stock__gte=stock)

    return render(request, 'core/listado_productos.html', data, {'stock':stock})

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

@permission_required('FloreriaPetalos/add_producto')
def eliminar_pelicula(request,id):
    peli=Pelicula.objects.get(name=id)
    mensaje=''
    try:
        peli.delete()
        mensaje='Pelicula Eliminada'
    except:
        mensaje='Problemas de Eliminacion Pelicula'

    pelis=Pelicula.objects.all()
    return render(request,'core/galeria.html',{'peliculas':pelis,'msg':mensaje})

@permission_required('FloreriaPetalos/add_producto')
def formulario(request):
    catego=Categoria.objects.all()# select * from categoria
    if request.POST:
        titulo=request.POST.get("txtTitulo")
        duracion=request.POST.get("txtDuracion")
        precio=request.POST.get("txtPrecio")
        descripcion=request.POST.get("txtDescripcion")
        categoria=request.POST.get("cboCategoria")
        #ubicamos de la tabla (modelo) Categoria el reg. con "name" igual al valor
        #recuperado del combo "cboCategoria"
        obj_categoria=Categoria.objects.get(name=categoria)
        imagen=request.FILES.get("imagen")
        #crear una instancia del modelo Pelicula
        pelicula=Pelicula(
            name=titulo,
            duracion=duracion,
            precio=precio,
            descripcion=descripcion,
            categoria=obj_categoria,
            imagen=imagen
        )
        pelicula.save() #se graba el contenido del objeto pelicula
        return render(request,'core/formulario.html',{'categorias':catego,'msg':'grabo'})
    return render(request,'core/formulario.html',{'categorias':catego})