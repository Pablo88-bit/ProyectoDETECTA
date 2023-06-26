from django.shortcuts import render #Plantillas
from .models import Alumnos, Profesor, Proveedor
from .models import Cursos, Materiales, MediosDidacticos
from django.shortcuts import render, redirect, get_object_or_404




# Create your views here.
def index(request):
    return render(request, 'nav_index.html')


def services(request):
    cursos = Cursos.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, 'nav_services.html', context)


def nosotros(request):
    profesor = Profesor.objects.all()
    context = {
        'profesor': profesor
    }
    return render(request, 'nav_nosotros.html', context)


def contacto(request):
    return render(request, 'nav_contacto.html')



#Enlaces del Footer
def procesos(request):
    return render(request, 'footer_procesos.html')    

def asistencia(request):
    return render(request, 'footer_asistencia.html')    

def consultas(request):
    return render(request, 'footer_consultas.html')

def asesoria(request):
    return render(request, 'footer_asesoria.html')

def terminos(request):
    return render(request, 'footer_terminos.html')

def politica(request):
    return render(request, 'footer_politica.html')


#Detalles
def cursodetalle(request, curso_id):
    curso = get_object_or_404(Cursos, id=curso_id)
    context = {
        'cursos': curso
    }
    return render(request, 'detallecurso.html', context)


def docentedetalle(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    context = {
        'profesor': profesor
    }
    return render(request, 'detalledocente.html', context)