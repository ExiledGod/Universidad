from django.db import models
from datetime import datetime, date
from Alumno.models import Alumno
from Profesor.models import Profesor 
# Create your models here.

class Alumno_en_Titulacion(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido_pat = models.CharField(max_length=100, blank=False, null=False)
    apellido_mat = models.CharField(max_length=100, blank=False, null=False)
    rut = models.CharField(max_length=13, null=False)
    mail = models.EmailField(max_length=254, blank=True, null=True)

    def __str__(self):
        cadena = self.nombre+" ("+self.rut+")"
        return cadena

class profeExaminador(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido_pat = models.CharField(max_length=100, blank=False, null=False)
    apellido_mat = models.CharField(max_length=100, blank=False, null=False)
    rut = models.CharField(max_length=13, null=False)
    mail = models.EmailField(max_length=254, blank=True, null=True)
    titulo = models.CharField(max_length=250, blank=True, null=True) #crear tabla

    def __str__(self):
        cadena = self.nombre+" ("+self.rut+")"
        return cadena

class comite(models.Model):
    profeExaminador = models.ForeignKey(profeExaminador, blank=True, null=True, on_delete=models.CASCADE)
    alumnoTitulo = models.ForeignKey(Alumno_en_Titulacion, blank=True, null=True, on_delete=models.CASCADE)
    coo = 'Correferente'
    externo = 'Externo'
    interno = 'Interno'
    director = 'Director'
    rol_choices = (
        (coo, u'Correferente'),
        (externo, u'Externo'),
        (interno, u'Interno'),
        (director, u'Director')
    )
    rol = models.CharField(max_length=20, choices=rol_choices, blank=False, null=True)

class estado(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateField(null=False, default=date.today)
    si = 'Si'
    no = 'No'
    valido_choices = (
        (si, u'Si'),
        (no, u'No'),
    )
    valido = models.CharField(max_length=20, choices=valido_choices, blank=False, null=True)

    def __str__(self):
        cadena = self.nombre+" estado:"+self.valido
        return cadena

class detalle(models.Model):
    detalle_estado = models.ForeignKey(Alumno_en_Titulacion, blank=True, null=True, on_delete=models.CASCADE)
    estado = models.ForeignKey(estado, blank=True, null=True, on_delete=models.CASCADE)

class entrega(models.Model):
    alumno = models.ForeignKey(Alumno_en_Titulacion, blank=True, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    fecha_entrega = models.DateField(null=False)
    nota = models.IntegerField()
    comentario = models.CharField(max_length=200, null=False, blank=False)
    archivo = models.FileField(upload_to=None, null=False, blank=False)
    primera_entrega = 'Primera Entrega'
    segunda_entrega = 'Segunda Entrega'
    entrega_choices = (
        (primera_entrega, u'Primera Entrega'),
        (segunda_entrega, u'Segunda Entrega'),
    ) 
    tipo = models.CharField(max_length=100, choices=entrega_choices, null=True, blank=True)
    
    def __str__(self):
        cadena = self.nombre+" "+self.fecha_entrega
        return cadena


class Titulacion(models.Model):
    alumno = models.ManyToManyField(Alumno, blank=True)
    nombre_titulacion = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField(null=False)

    def __str__(self):
        return self.nombre_titulacion

class enviar_email(models.Model):
    alumno = models.ForeignKey(Alumno_en_Titulacion, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=False, blank=False)
    mensaje = models.CharField(max_length=1000, null=False, blank=True)

    def __str__(self):
        return self.nombre

class inscripcion_tema(models.Model):
    alumno = models.ForeignKey(Alumno_en_Titulacion, null=True, blank=True, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, null=True, blank=True, on_delete=models.CASCADE)
    nombre_tema = models.CharField(max_length=200, null=True, blank=True)
