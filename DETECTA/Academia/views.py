from django.shortcuts import render #Plantillas
from .models import Cursos
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')


def services(request):
    cursos = Cursos.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, 'services.html', context)


def nosotros(request):
    return render(request, 'nosotros.html')


def contacto(request):
    return render(request, 'contacto.html')



#Enlaces del Footer
def procesos(request):
    return render(request, 'procesos.html')    


def terminos(request):
    return render(request, 'terminos.html')


def politica(request):
    return render(request, 'politica.html')
