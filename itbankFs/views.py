from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def prestamos(request):
    return render(request,'prestamos.html')

def atCliente(request):
    return render(request, 'atCliente.html')

def seguros(request):
    return render(request, 'seguros.html')

def tarjetas(request):
    return render(request, 'tarjetas.html')

def dolarHoy(request):
    return render(request,'dolarHoy.html')

def calculadora(request):
    return render(request, 'calculadora.html')