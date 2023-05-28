from django.urls import path, include 
from . import views
#from .views import dash_view

urlpatterns = [
    path('', views.index, name="index"),
    path('servicios/', views.services, name="services"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('graficos/', views.graficos, name="graficos"),
    path("change-theme/", views.change_theme, name="change_theme"),
    #path('the_django_plotly_dash/', include('django_plotly_dash.urls', namespace='the_django_plotly_dash')),
]