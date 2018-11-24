from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'index.html')


def listado(request):
    return render(request, 'crud/listar.html')


def agregar_crud(request):
    return render(request, 'crud/agregar.html')