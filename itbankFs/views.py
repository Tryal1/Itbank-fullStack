from django.shortcuts import render

from .forms import loginForm,RegisterForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# Create your views here.
formLogin = loginForm()
formRegister = RegisterForm()


print(authenticate,'aca')

def home(request):
    userComplete = None
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        pin = request.POST.get('pin')
        userComplete = authenticate(request,user=user,password=password,pin=pin)
    if userComplete is not None:
        print('login')
    else:
        print('login_required')
    return render(request, 'index.html', {'form': formLogin,'formRegister':formRegister})


def prestamos(request):
    return render(request, 'prestamos.html', {'form': formLogin})


def atCliente(request):
    return render(request, 'atCliente.html', {'form': formLogin})


def seguros(request):
    return render(request, 'seguros.html', {'form': formLogin})


def tarjetas(request):
    return render(request, 'tarjetas.html', {'form': formLogin})


def dolarHoy(request):
    return render(request, 'dolarHoy.html', {'form': formLogin})


def calculadora(request):
    return render(request, 'calculadora.html')

def clientes(request):
    return render(request, 'clientes.html')

def cuentas(request):
    return render(request, 'cuentas.html')