from django.urls import path
from . import views
#from .views import dash_view

urlpatterns = [
    path('', views.index, name="index"),
    path('servicios/', views.services, name="services"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('contacto/', views.contacto, name="contacto"),
    path('procesos/', views.procesos, name="procesos"),
    path('asistencia/', views.asistencia, name="asistencia"),
    path('consultas/', views.consultas, name="consultas"),
    path('asesoria/', views.asesoria, name="asesoria"),
    path('terminos/', views.terminos, name="terminos"),
    path('politica/', views.politica, name="politica"),
    path('curso/detalle/<int:curso_id>/', views.cursodetalle, name='cursodetalle'),
    path('docente/detalle/<int:profesor_id>/', views.docentedetalle, name='docentedetalle'),
    #path('chart-data/alumnos/', views.chart_data_alumnos, name='chart_data_alumnos'),
    #path('formulario/alumno/', views.formulario_modelo_alumno, name='formulario_modelo_alumno'),
    #path('the_django_plotly_dash/', include('django_plotly_dash.urls', namespace='the_django_plotly_dash')),
]