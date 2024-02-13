from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('FormularioCliente/', views.formulario_cliente, name="Formularios Clientes"),
    path('FormularioEmpleado/', views.formulario_empleado, name="Formularios Empleado"),
    path('FormularioArticulo/', views.formulario_articulo, name="Formularios Articulo"),
    
]