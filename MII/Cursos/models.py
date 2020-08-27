from django.db import models
from Alumno.models import Alumno
from Profesor.models import Profesor
from datetime import datetime, timedelta
import time
# Create your models here.
class Lista_alumnos(models.Model):
	id_lista = models.BigAutoField(null=False, primary_key=True)
	alumno = models.ManyToManyField(Alumno, blank=True)

	def __str__(self):
		return self.id_lista


	def to_dict_json(self):
		return {
			'id': self.id,
			'alumno_id': self.alumno_id,
		}

class Cursos(models.Model):
	nombre = models.CharField(max_length=300, null=False)
	sigla = models.CharField(max_length=10, null=False)
	creditos = models.IntegerField(null=True, blank=True)
	optativo = 'Optativo'
	obligatorio = 'Obligatorio'
	nivelacion = 'Nivelacion'
	tipo_curso_choices = (
		(optativo, u'Optativo'),
		(obligatorio, u'Obligatorio'),
		(nivelacion, u'Nivelacion'),
	)
	tipo = models.CharField(max_length=12, choices=tipo_curso_choices, blank=False, null=False)
	nuevo = 'Nueva'
	antiguo = 'Antigua'
	tipo_curso_malla = (
		(nuevo, u'Nueva'),
		(antiguo, u'Antigua'),
	)
	curso_en_malla = models.CharField(max_length=40, choices=tipo_curso_malla, blank=False, null=False, default=nuevo)
	descripcion = models.CharField(max_length=1000, blank=True, null=True)


	class Meta:
		ordering = ('nombre', 'sigla', 'creditos')
		verbose_name='Curso'
		verbose_name_plural='Cursos'


	def __str__(self):
		cadena = self.nombre+" ("+self.sigla+")"
		return cadena


	def to_dict_json(self):
		return {
			'id': self.id,
			'nombre': self.nombre,
			'sigla': self.sigla,
			'creditos': self.creditos,
			'tipo': self.get_tipo_display(),
			'descripcion': self.descripcion,
		}

class semestre1(models.Model):
	curso = models.ManyToManyField(Cursos, blank=True)

class semestre2(models.Model):
	curso = models.ManyToManyField(Cursos, blank=True)

class semestre3(models.Model):
	curso = models.ManyToManyField(Cursos, blank=True)

class trimestral(models.Model):
	curso = models.ManyToManyField(Cursos, blank=True)

class Detalle_curso(models.Model):
	profesor = models.ForeignKey(Profesor, null=True, blank=True, on_delete=models.CASCADE)
	lista_alumnos = models.ForeignKey(Lista_alumnos, null=True, blank=True, on_delete=models.CASCADE)
	curso = models.ForeignKey(Cursos, null=True, blank=True, on_delete=models.CASCADE)
	anio_cursado = models.CharField(max_length=4, null=False, blank=True)
	semestre = models.CharField(max_length=2, null=False, blank=True)
	paralelo = models.IntegerField(null=False)
	aprobados = models.CharField(max_length=300, null=True,blank=True)
	rechazados = models.CharField(max_length=300, null=True, blank=True)
	descripcion = models.CharField(max_length=500, null=True, blank=True)
	inscritos = models.CharField(max_length=500, null=True, blank=True)

	class Meta:
		ordering= ('anio_cursado', 'semestre', 'curso')
		verbose_name='Detalle'
		verbose_name_plural='Detalles'

	def __str__(self):
		cadena = self.anio_cursado
		return cadena

	def to_dict_json(self):
		return {
			'id': self.id,
			'lista_alumnos_id': self.lista_alumnos_id,
			'profesor_id': self.profesor_id,
			'curso_id': self.curso_id,
			'anio_cursado': self.anio_cursado,
			'semestre': self.semestre,
			'paralelo': self.paralelo,
			'aprobados': self.aprobados,
			'rechazados': self.rechazados,
			'descripcion': self.descripcion,
			'inscritos': self.inscritos,
		}


class AvanceCurricular(models.Model):
	alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	semestre1 = models.ForeignKey(semestre1, null=True, blank=True, on_delete=models.CASCADE)
	semestre2 = models.ForeignKey(semestre2, null=True, blank=True, on_delete=models.CASCADE)
	semestre3 = models.ForeignKey(semestre3, null=True, blank=True, on_delete=models.CASCADE)
	trimestral = models.ForeignKey(trimestral, null=True, blank=True, on_delete=models.CASCADE)
	semestre_1 = '1er Semestre'
	semestre_2 = '2do Semestre'
	semestre_choices = (
		(semestre_1, u'1er Semestre'),
		(semestre_2, u'2do Semestre'),
	)
	semestre = models.CharField(max_length=50, choices=semestre_choices, null=True, blank=True)
	anio_cursado = models.CharField(max_length=4, null=False, blank=True)
	en_proceso = 'En proceso'
	aprobado = 'Aprobado'
	rechazado = 'Rechazado'
	retiro = 'Retiro'
	opciones = (
		(en_proceso, u'En proceso'),
		(aprobado, u'Aprobado'),
		(rechazado, u'Rechazado'),
		(retiro, u'Retiro'),
	)
	estado = models.CharField(max_length=300, choices=opciones, blank=False, null=False)
	anio_actual = time.strftime("%Y")


	class Meta:
		ordering= ('anio_cursado', 'estado')
		verbose_name='Avance'
		verbose_name_plural='Avances'

	def __str__(self):
		cadena = self.alumno.nombre+" "+self.alumno.apellido_pat+" "+ self.alumno.apellido_mat
		return cadena

	def to_dict_json(self):
		return {
			'id': self.id,
			'estado': self.get_estado_display(),
		}


class Malla_curricular(models.Model):
	curso = models.ForeignKey(Cursos, null=True, blank=True, on_delete=models.CASCADE)
	nueva = 'Malla Nueva'
	antigua = 'Malla Antigua'
	malla_opciones = (
		(nueva, u'Malla Nueva'),
		(antigua, u'Malla Antigua')
	)
	malla = models.CharField(max_length=40, null=False, blank=False)