from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import Curso,Entregable,Estudiante,Profesor
def inicio(request):
    return render(request,"WebApp/index.html")

def cursos(request): 
    query = request.GET.get("q")
    if query:
        curso = Curso.objects.filter(curso__icontains=query)
        return render(request,"WebApp/busqueda.html")
    else:
        curso = Curso.objects.all()
        return render(request, "WebApp/cursos.html", {"curso": curso})
    #return render(request,"WebApp/cursos.html")

def profesores(request):
    return render(request,"WebApp/profesores.html")

def estudiantes(request):
    return render(request,"WebApp/estudiantes.html")

def entregables(request):
    return render(request,"WebApp/entregables.html")

def formulario_curso(request):
    if request.method == "POST":
        curso = Curso(curso=request.POST["curso"],comision=request.POST["comision"])
        curso.save()
        #return render(request,"WebApp/forms/formulario_curso.html")
        return redirect("cursos")
    else:
        return render(request,"WebApp/forms/formulario_curso.html")