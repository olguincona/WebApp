from django.urls import path
from WebApp.views import inicio,cursos,profesores,estudiantes,entregables,formulario_curso

urlpatterns = [
    path('inicio/',inicio,name="inicio"),
    path('cursos/',cursos,name="cursos"),
    path('profesores/',profesores,name="profesores"), 
    path('estudiantes/',estudiantes,name="estudiantes"),
    path('entregables/',entregables,name="entregables"),
    path('formulario_curso/',formulario_curso,name="formulario_curso"),
]