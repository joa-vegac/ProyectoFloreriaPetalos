from django.shortcuts import render
from .models import Producto

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def registro(request):
    return render(request, 'core/registro.html')

def catalogo(request):
    productos=Producto.objects.all()
    return render(request, 'core/catalogo.html',{'productos': productos})
  
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
        product.save
    return render(request,'core/registro_producto.html')
    

