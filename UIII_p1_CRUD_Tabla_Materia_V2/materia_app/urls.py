from django.urls import path
from . import views
urlpatterns = [
    path('',views.inicio_vistas,name='gestionarMateria.html'),
    path('registrarMateria/',views.registrarMateria,  name='registrarMateria'),

]