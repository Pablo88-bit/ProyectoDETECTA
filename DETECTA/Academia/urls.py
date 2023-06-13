from django.urls import path
from . import views
#from .views import dash_view

urlpatterns = [
    path('', views.index, name="index"),
    path('servicios/', views.services, name="services"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('contacto/', views.contacto, name="contacto"),
    path('procesos/', views.procesos, name="procesos"),
    path('terminos/', views.terminos, name="terminos"),
    path('politica/', views.politica, name="politica"),
    #path('chart-data/alumnos/', views.chart_data_alumnos, name='chart_data_alumnos'),
    #path('formulario/alumno/', views.formulario_modelo_alumno, name='formulario_modelo_alumno'),
    #path('the_django_plotly_dash/', include('django_plotly_dash.urls', namespace='the_django_plotly_dash')),
]