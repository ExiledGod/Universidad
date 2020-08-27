from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EstadoTarea(models.Model):
    estado = models.CharField(max_length = 255)
    def __str__(self):
        return (self.estado)

class TipoTarea(models.Model):
    Tipo = models.CharField(max_length = 255)
    def __str__(self):
        return (self.Tipo)

class Edificio(models.Model):
    Name_build = models.CharField(max_length=255)
    Ubicacion = models.CharField(max_length=255)
    def __str__(self):
        return (self.Name_build+" "+self.Ubicacion)

class Sala(models.Model):
    sala = models.CharField(max_length=255)
    def __str__(self):
        return (self.sala)

class Tarea(models.Model):
    titulo = models.CharField(max_length = 255)
    descripcion = models.CharField(max_length = 255)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    fechaInicio = models.DateField("%d-%m-%Y")
    fechaTermino = models.DateField("%d-%m-%Y", null=True, blank=True)
    edificio = models.ForeignKey('Edificio', on_delete=models.DO_NOTHING)
    sala = models.ForeignKey('Sala', on_delete=models.DO_NOTHING)
    estadoTarea = models.ForeignKey('EstadoTarea', on_delete = models.DO_NOTHING)
    tipoTarea = models.ForeignKey('TipoTarea', on_delete = models.DO_NOTHING)
    def __str__(self):
        return (self.titulo)


