from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime
from .models import cliente, empleado, articulo

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
        cliente1 = cliente(request.post["nombre"], request.post["fecha_nacimiento"], request.post["email"])
        cliente1.save()
        #return HttpResponse("todo ok")
        return render(request, 'template1bis.html')
    return render(request, 'template1bis.html')


def formulario_empleado(request):
    if request.method == "POST":
        empleado1 = empleado(request.post["nombre"], request.post["fecha_nacimiento"], request.post["email"], request.post["profesion"])
        empleado1.save()
        #return HttpResponse("todo ok")
        return render(request, 'template3.html')
    return render(request, 'template3.html')


def formulario_articulo(request):
    if request.method == "POST":
        articulo1 = articulo(request.post["nombre"], request.post["modelo"])
        articulo1.save()
        #return HttpResponse("todo ok")
        return render(request, 'template3.html')
    return render(request, 'template3.html')