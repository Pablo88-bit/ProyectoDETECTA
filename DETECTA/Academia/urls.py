from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.index, name="index"),
    path('servicios/', views.services, name="services"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('TerminosCondiciones/', views.TerminosCondiciones, name="TerminosCondiciones"),
]