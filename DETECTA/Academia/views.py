from django.shortcuts import render #Plantillas

# Create your views here.
def index(request):
    return render(request, 'index.html')


def services(request):
    return render(request, 'services.html')


def nosotros(request):
    return render(request, 'nosotros.html')

def TerminosCondiciones(request):
    return render(request, 'TerminosCondiciones.html')

def PoliticaPrivacidad(request):
    return render(request, 'PoliticaPrivacidad.html')

def AvisoLegal(request):
    return render(request, 'AvisoLegal.html')
