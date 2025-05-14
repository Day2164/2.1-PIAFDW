from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def ofertas(request):
    return render(request, 'ofertas.html')

def productos(request):
    return render(request, 'productos.html')