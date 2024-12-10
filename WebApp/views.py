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
        if request.method == "POST":
            curso = Curso(curso=request.POST["curso"],comision=request.POST["comision"])
            curso.save()
            return render(request,"WebApp/busqueda.html")
    else:
        curso = Curso.objects.all()
        return render(request, "WebApp/cursos.html", {"curso": curso})
    #return render(request,"WebApp/cursos.html")

def profesores(request):
    query = request.GET.get("q")
    if query:
        nombre = Profesor.objects.filter(nombre__icontains=query)
        if request.method == "POST":
            nombre = Profesor(nombre=request.POST["nombre"],apellido=request.POST["apellido"],email=request.POST["email"],profesion=request.POST["profesion"])
            nombre.save()
            return render(request,"WebApp/busqueda.html")
    else:
        nombre = Curso.objects.all()
        return render(request, "WebApp/profesores.html", {"nombre": nombre})
    #return render(request,"WebApp/profesores.html")

def estudiantes(request):
    query = request.GET.get("q")
    if query:
        nombre = Profesor.objects.filter(nombre__icontains=query)
        if request.method == "POST":
            nombre = Profesor(nombre=request.POST["nombre"],apellido=request.POST["apellido"],email=request.POST["email"])
            nombre.save()
            return render(request,"WebApp/busqueda.html")
    else:
        nombre = Curso.objects.all()
        return render(request, "WebApp/estudiantes.html", {"nombre": nombre})
    #return render(request,"WebApp/estudiantes.html")

def entregables(request):
    query = request.GET.get("q")
    if query:
        nombre = Profesor.objects.filter(nombre__icontains=query)
        if request.method == "POST":
            nombre = Profesor(nombre=request.POST["nombre"],fechaDeEntrega=request.POST["fecha"])
            nombre.save()
            return render(request,"WebApp/busqueda.html")
    else:
        nombre = Curso.objects.all()
        return render(request, "WebApp/entregables.html", {"nombre": nombre})
    #return render(request,"WebApp/entregables.html")

def formulario_curso(request):
    if request.method == "POST":
        curso = Curso(curso=request.POST["curso"],comision=request.POST["comision"])
        curso.save()
        #return render(request,"WebApp/forms/formulario_curso.html")
        return redirect("cursos")
    else:
        return render(request,"WebApp/forms/formulario_curso.html")