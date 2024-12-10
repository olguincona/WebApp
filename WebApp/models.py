from django.db import models

class Curso (models.Model):
    curso = models.CharField(max_length=30) # Campo string de 100 caracteres 
    comision = models.IntegerField() # Campo entero
    def __str__(self):
        return f"Nombre del Curso: {self.curso} - N° de Comisión: {self.comision}"

class Estudiante (models.Model):
    nombre = models.CharField(max_length=30) # Campo string de 100 caracteres 
    apellido = models.CharField(max_length=30) # Campo string de 100 caracteres 
    email = models. EmailField() # Campo de email

class Profesor (models.Model):
    nombre = models.CharField(max_length=30) # Campo string de 30 caracteres 
    apellido = models.CharField(max_length=30) # Campo string de 30 caracteres 
    email = models. EmailField() # Campo de email
    profesion = models.CharField(max_length=50) # Campo string de 50 caracteres

class Entregable(models.Model):
    nombre = models.CharField(max_length=100) # Campo string de 100 caracteres 
    fechaDeEntrega = models.DateField() # Campo de fecha
    entregado = models. BooleanField() # Campo booleano

