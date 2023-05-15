from django.shortcuts import render #Plantillas
#from django.http import HttpResponse
#from dash import app

# Create your views here.
def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def nosotros(request):
    return render(request, 'nosotros.html')


def graficos(request):
    return render(request, 'graficos.html')