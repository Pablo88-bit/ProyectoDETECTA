from django.shortcuts import render #Plantillas
from .models import Cursos
#from django.http import HttpResponse
#from dash import app
from .models import Temas
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

#Sin terminar los temas
def change_theme(request):
    if request.method == "POST":
        theme = request.POST.get("tema")
        user_theme, created = Temas.objects.get_or_create(user=request.user)
        user_theme.tema = theme
        user_theme.save()
        messages.success(request, "Tema cambiado exitosamente.")
        return redirect("admin:index")
    else:
        return redirect("admin:index")

def graficos(request):
    return render(request, 'graficos.html')