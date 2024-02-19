from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime
from .models import cliente, empleado, articulo
from myapp.forms import clienteFormulario, empleadoFormulario, articuloFormulario

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# def cursos_formularios(request):
#     if request.method == 'POST':
#         mi_formulario = CursoFormulario(request.POST) #es donde nos llega la informacion del html
        
#         if mi_formulario.is_valid():
#             informacion = mi_formulario.cleaned_data
#             print(informacion)
#             cliente1 = cliente(informacion["nombre"], informacion["fecha_nacimiento"], informacion["email"])
#             cliente1.save()
#             return render(request, 'cursos_formulario.html')

#     else:
#         mi_formulario = CursoFormulario()
#         return render(request, 'cursos_formulario.html', {"mi_formulario": mi_formulario})
    

def formulario_cliente(request):
    if request.method == "POST":
        mi_formulario = clienteFormulario(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente1 = cliente(nombre=informacion["nombre"], fecha_nacimiento=informacion["fecha_nacimiento"], email=informacion["email"])
            cliente1.save()
            return render(request, 'cargaExitosa.html')
        else:
            plantilla = loader.get_template('cargaFallida.html')
            documento = plantilla.render()
            return HttpResponse(documento)

    else:
        mi_formulario = clienteFormulario()
        return render(request, 'cliente_bootstrapp.html', {"mi_formulario": mi_formulario})
    


def formulario_empleado(request):
    if request.method == "POST":
        mi_formulario = empleadoFormulario(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            empleado1 = empleado(nombre=informacion["nombre"], fecha_nacimiento=informacion["fecha_nacimiento"], email=informacion["email"], puesto=informacion["puesto"])
            empleado1.save()
            #return HttpResponse("todo ok")
            return render(request, 'cargaExitosa.html')
        else:
            plantilla = loader.get_template('cargaFallida.html')
            documento = plantilla.render()
            return HttpResponse(documento)
        
    else:
        mi_formulario = empleadoFormulario()
        return render(request, 'empleado_bootstrapp.html', {"mi_formulario": mi_formulario})
    


def formulario_articulo(request):
    if request.method == "POST":
        mi_formulario = articuloFormulario(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            articulo1 = articulo(nombreArticulo=informacion["nombreArticulo"], modelo=informacion["modelo"])
            articulo1.save()
            #return HttpResponse("todo ok")
            return render(request, 'cargaExitosa.html')
        
        else:
            plantilla = loader.get_template('cargaFallida.html')
            documento = plantilla.render()
            return HttpResponse(documento)
        
    else:
        mi_formulario = empleadoFormulario()
        return render(request, 'articulo_bootstrapp.html', {"mi_formulario": mi_formulario})
        
 
def buscar_articulo(request):
    
     if request.GET['nombreArticulo']:
         nombre_articulo = request.GET['nombreArticulo']
         modelo_articulo = articulo.objects.filter(nombreArticulo__icontains=nombre_articulo)
         return render(request, 'busquedaArticulo.html', { 'nombreArticulo': nombre_articulo, 'modelo':modelo_articulo})
     else:
         respuesta = 'No enviaste datos'
        
     return render(request, 'busquedaArticulo.html', {'respuesta': respuesta})


     