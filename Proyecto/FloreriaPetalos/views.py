from django.shortcuts import render
from .models import Producto
from django.contrib.auth.decorators import login_required

# Create your views here.

def registro(request):
     return render(request, 'core/registro.html')

def login(request):
    return render(request, 'core/login.html')

def index(request):
    return render(request, 'core/index.html')

def catalogo(request):
    return render(request, 'core/catalogo.html')
  
def registro_producto(request):
    if request.POST:
        accion=request.POST.get("RegProduct")
        if accion=='aceptar':            
            nombre=request.POST.get("Name")
            valor=request.POST.get("Value")
            desc=request.POST.get("Desc")
            image=request.FILES.get("Image")
            stock=request.POST.get("Stock")

            product=Producto(
                nombre=nombre,
                valor=valor,
                desc=desc,
                image=image,
                stock=stock,
            )
            product.save()
    return render(request,'core/registro_producto.html')
    

