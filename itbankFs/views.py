from django.shortcuts import render

from django.contrib.auth.models import User

from .forms import loginForm, RegisterForm, Prestamos
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from .models import Cuenta, Cliente, Tarjeta


# Create your views here.
formLogin = loginForm()
formRegister = RegisterForm()


def home(request):
    if request.method == 'POST':

        # dentro del template del form, está el nombre "register" dentro del submit del form
        # de esta manera podemos diferenciar cuál es el formulario que se está enviando
        if 'register' in request.POST:

            dni = request.POST['dni']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']

            # se chequea que las contraseñas coincidan
            if password == password2:

                # se crea el usuario con los datos ingresados
                # user = User.objects.create_user()
                user = User.objects.create_user(
                    username=dni, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()

                messages.success(request, 'Usuario creado correctamente')

                return HttpResponseRedirect('/')

            else:

                messages.error(request, 'Pin incorrecto')

                return HttpResponseRedirect('')

        # si se completó el formulario de login
        if 'login' in request.POST:

            dni = request.POST['dni']
            password = request.POST['password']
            user = authenticate(username=dni, password=password)

            if user is not None and password is not None:

                login(request, user)

                return HttpResponseRedirect('/')

            else:

                messages.error(request, 'Usuario o contraseña incorrectos')
                return HttpResponseRedirect('/')

        if 'logaut' in request.POST:
            logout(request)
            return HttpResponseRedirect('/')

    return render(request, 'index.html', {'form': formLogin, 'formRegister': formRegister})


def prestamos(request):
    prestamos = Prestamos()
    return render(request, 'prestamos.html', {'form': formLogin, 'formRegister': formRegister, 'prestamos': prestamos})


def atCliente(request):
    return render(request, 'atCliente.html', {'form': formLogin, 'formRegister': formRegister})


def seguros(request):
    return render(request, 'seguros.html', {'form': formLogin, 'formRegister': formRegister})


def tarjetas(request):
    return render(request, 'tarjetas.html', {'form': formLogin, 'formRegister': formRegister})


def dolarHoy(request):
    return render(request, 'dolarHoy.html', {'form': formLogin, 'formRegister': formRegister})


def calculadora(request):
    return render(request, 'calculadora.html', {'form': formLogin, 'formRegister': formRegister})


def cuentas(request):
    return render(request, 'cuentas.html', {'form': formLogin, 'formRegister': formRegister})


def clientes(request):

    user = Cliente.objects.get(customer_dni=User.get_username(request.user))
    cuenta = Cuenta.objects.get(account_id=user.customer_id)
    # ACA FALTA EL DE TARJETA    
    print(cuenta.balance)
    context = {
        "user": user,
        "cuenta": cuenta,
    }
    return render(request, 'clientes.html' ,{'form': formLogin, 'formRegister': formRegister,'context':context})
