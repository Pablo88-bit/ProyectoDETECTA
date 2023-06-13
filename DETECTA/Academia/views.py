from django.shortcuts import render #Plantillas
from .models import Alumnos, Profesor, Proveedor
from .models import Cursos, Materiales, MediosDidacticos
from django.shortcuts import render, redirect
from django.contrib import messages
#Gráficos
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.db.models import Count, Avg



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


""" 
#Gráficos
@require_GET
def chart_data_alumnos(request):
    # Obtener los datos seleccionados del formulario
    tipo_grafico = request.GET.get('tipo_grafico')
    datos_grafico_id = request.GET.get('datos_grafico')

    # Obtener los datos necesarios para el gráfico de Alumnos
    if tipo_grafico == 'pastel':
        # Procesar los datos para el gráfico de pastel
        # Ejemplo: contar la cantidad de alumnos por nacionalidad
        data = Alumnos.objects.values(datos_grafico_id).annotate(count=Count('id'))
        labels = [entry[datos_grafico_id] for entry in data]
        values = [entry['count'] for entry in data]
    elif tipo_grafico == 'barras':
        # Procesar los datos para el gráfico de barras
        # Ejemplo: obtener el promedio de notas de los alumnos por año de ingreso
        data = Alumnos.objects.values(datos_grafico_id).annotate(average=Avg('nota'))
        labels = [entry[datos_grafico_id] for entry in data]
        values = [entry['average'] for entry in data]
    else:
        # Tipo de gráfico no válido
        labels = []
        values = []

    # Crear el diccionario de datos del gráfico
    chart_data = {
        'labels': labels,
        'data': values,
        'chart_type': tipo_grafico  # Agrega el tipo de gráfico seleccionado al contexto
    }

    return render(request, 'grafico.html', chart_data)
    #return JsonResponse(chart_data)


# Vista del formulario del modelo
def formulario_modelo_alumno(request):
    # Procesa los datos del formulario y obtén los datos para el gráfico
    # (puedes ajustar esto según los campos y datos que necesites)
    tipo_grafico = request.POST.get('tipo_grafico')
    datos_grafico_id = request.POST.get('datos_grafico')

    # Llama a la función de vista chart_data_alumnos para obtener los datos del gráfico
    chart_data = chart_data_alumnos(request)

    # Agrega los datos del gráfico al contexto del formulario
    contexto = {
        'tipo_grafico': tipo_grafico,
        'datos_grafico_id': datos_grafico_id,
        'chart_data': chart_data
    }

    # Renderiza la plantilla del formulario y pasa el contexto
    return render(request, 'formularioalumnos.html', contexto) """