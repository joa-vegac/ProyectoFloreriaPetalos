from django.shortcuts import render
from .models import Producto
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'core/login.html')
    
def registro(request):
    return render(request, 'core/registro.html')

@login_required(login_url='/login/')
def index(request):
    return render(request, 'core/index.html')

@login_required(login_url='/login/')
def catalogo(request):
    productos=Producto.objects.all()
    return render(request, 'core/catalogo.html',{'productos': productos})

@login_required(login_url='/login/')
def registro_producto(request):
    if request.POST:
        accion=request.POST.get("accion")
        if accion=='registrar':
            prdctnombre = request.POST.get("name")
            prdctvalor = request.POST.get("value")
            prdctdescripcion = request.POST.get("desc")
            prdctstock = request.POST.get("stock")
            prdctimagen= request.FILES.get("image")

        product=Producto(
            nombre= prdctnombre,
            valor= prdctvalor,
            descripcion= prdctdescripcion,
            stock= prdctstock,
            imagen= prdctimagen
        )
        product.save()
        return render(request, 'core/registro_producto.html', {'msg':'Producto registrado'})
    return render(request,'core/registro_producto.html')

