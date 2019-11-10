from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    return render(request, 'core/login.html')

def login_acceso(request):
    if request.POST:
        email=request.POST.get("txtEmail")
        password=request.POST.get("txtPass")

        user = authenticate(request, email=email, password=password)

@login_required(login_url='/login/')

def index(request):
    return render(request, 'core/index.html')

def catalogo(request):
    return render(request, 'core/catalogo.html')

def registro(request):
    return render(request, 'core/registro.html')

@login_required(login_url='/login/')    
def registro_producto(request):
    return render(request, 'core/registro_producto.html')
