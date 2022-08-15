from django.shortcuts import render

from .forms import loginForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# Create your views here.
form = loginForm()


def home(request):
    return render(request, 'index.html', {'form': form})


def prestamos(request):
    return render(request, 'prestamos.html', {'form': form})


def atCliente(request):
    return render(request, 'atCliente.html', {'form': form})


def seguros(request):
    return render(request, 'seguros.html', {'form': form})


def tarjetas(request):
    return render(request, 'tarjetas.html', {'form': form})


def dolarHoy(request):
    return render(request, 'dolarHoy.html', {'form': form})


def calculadora(request):
    return render(request, 'calculadora.html')

def clientes(request):
    return render(request, 'clientes.html')

def cuentas(request):
    return render(request, 'cuentas.html')