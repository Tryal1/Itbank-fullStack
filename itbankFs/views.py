from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def prestamos(request):
    return render(request,'prestamos.html')