from smart_selects.db_fields import ChainedForeignKey, GroupedForeignKey
from django.db import models
from Direccion.models import Region, Provincia, Comuna
from itertools import cycle
from .validators import digito_verificador


# Create your models here.
class Becas(models.Model):
	id_beca = models.BigAutoField(null=False, primary_key=True)
	nombre = models.CharField(max_length=100, null=False)
	monto = models.CharField(max_length=9, null=False)
	continuidad = 'Continuidad de Estudios'
	destacado = 'Alumno Destacado'
	alumni = 'Alumni PUCV'
	tipo_choices = (
		(continuidad, u'Continuidad de Estudios'),
		(destacado, u'Alumno Destacado'),
		(alumni, u'Alumni PUCV'),
	)
	tipo = models.CharField(max_length=100, choices=tipo_choices, blank=False, null=False)

	def __str__(self):
		cadena = self.nombre+" ("+self.tipo+")"
		return cadena

class Alumno(models.Model):
	becas = models.ManyToManyField(Becas, blank=True)
	nombre = models.CharField(max_length=150, blank=False)
	apellido_pat = models.CharField(max_length=30, null=False, blank=False)
	apellido_mat = models.CharField(max_length=30, null=False, blank=False)
	rut = models.CharField(max_length=13, null=False, validators=[digito_verificador])
	telefono = models.CharField(max_length=12, null=True)
	fecha_nac = models.DateField(null=False)
	nacionalidad = models.CharField(max_length=300, null=False, blank=False, default='Chilena')
	sexo_masculino = 'Masculino'
	sexo_femenino = 'Femenino'
	sexo_otro = 'Otro'
	sexo_choices = (
		(sexo_masculino, u'Masculino'),
		(sexo_femenino, u'Femenino'),
		(sexo_otro, u'Otro'),
	)
	sexo = models.CharField(max_length=20, choices=sexo_choices, blank=False, null=True)
	primer_semestre = 'Primer Semestre'
	segundo_semestre = 'Segundo Semestre'
	primer_trimestre = 'Primer Trimestre'
	segundo_trimestre = 'Segundo Trimestre'
	tercer_trimestre = 'Tercer Trimestre'
	cuarto_trimestre = 'Cuarto Trimeste'
	semestre_ingreso_choices = (
		(primer_semestre, u'Primer Semestre'),
		(segundo_semestre, u'Segundo Semestre'),
		(primer_trimestre, u'Primer Trimestre'),
		(segundo_trimestre, u'Segundo Trimestre'),
		(tercer_trimestre, u'Tercer Trimestre'),
		(cuarto_trimestre, u'Cuarto Trimestre'),
	)
	semestre_ingreso = models.CharField(max_length=300, choices=semestre_ingreso_choices, blank=True, null=True)
	anio_ingreso = models.IntegerField(null=False, default=2019)
	mail = models.EmailField(max_length=300, blank=True, null=True)
	beca = models.BooleanField(null=False, blank=False, default=False)
	matriculado = 'Matriculado'
	postulante = 'Postulante'
	en_espera = 'En Espera'
	rechazado = 'Rechazado'
	estado_choices = (
		(matriculado, u'Matriculado'),
		(postulante, u'Postulante'),
		(en_espera, u'En Espera'),
		(rechazado, u'Rechazado'),
	)
	estado = models.CharField(max_length=300, choices=estado_choices, blank=False, null=True)


	class Meta:
		ordering = ('nombre',)
		verbose_name= 'Alumno'
		verbose_name_plural = 'Alumnos'


	def __str__(self):
		cadena = self.nombre+" "+self.apellido_pat+" "+self.apellido_mat+" ("+self.rut+")"
		return cadena


	def to_dict_json(self):
		return {
			'id': self.id,
			'nombre': self.nombre,
			'apellido_pat': self.apellido_pat,
			'apellido_mat': self.apellido_mat,
			'rut': self.rut,
			'telefono': self.telefono,
			'fecha_nac': self.fecha_nac,
			'sexo': self.get_sexo_display(),
			'mail': self.mail
		}


class Cursos_homologados(models.Model):
	alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
	id_curso = models.BigAutoField(null=False, primary_key=True)
	nombre = models.CharField(max_length=100, null=False)

	class Meta:
		ordering = ('nombre',)
		verbose_name= 'Cursos_homologado'
		verbose_name_plural = 'Cursos_homologados'


	def __str__(self):
		return self.nombre


	def to_dict_json(self):
		return {
			'id': self.id,
			'nombre': self.nombre
		}


class Postulacion(models.Model):
	alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	fecha_post = models.DateField(null=False)
	universidad_procedencia = models.CharField(max_length=100, null=False)
	carrera_procedencia = models.CharField(max_length=100, null=False)
	nivelacion_si = 'Necesita'
	nivelacion_no = 'No necesita'
	nivelacion_choices = (
		(nivelacion_si, u'Necesita'),
		(nivelacion_no, u'No necesita'),
	)
	nivelacion = models.CharField(max_length=30, choices=nivelacion_choices, blank=False, null=False)
	semestre_ingreso = models.CharField(max_length=30, null=True, blank=True)	
	anio_ingreso = models.CharField(max_length=30, null=True, blank=True)
	estado_activo = 'Activo'
	estado_inactivo = 'Inactivo'
	estado_choices = (
		(estado_activo, u'Activo'),
		(estado_inactivo, u'Inactivo'),
	)
	estado_matricula = models.CharField(max_length=20, choices=estado_choices, blank=False, null=True)
	antecedentes_academicos = models.IntegerField(null=True)
	antecedentes_profesionales = models.IntegerField(null=True)
	carta_recomendacion = models.IntegerField(null=True)
	entrevista = models.CharField(max_length=30, null=True)
	puntaje = models.IntegerField(null=True)
	aprueba_condicion = 'Aprueba'
	reprueba_condicion = 'Reprueba'
	resultadoCondicion_choices = (
		(aprueba_condicion, u'Aprueba'),
		(reprueba_condicion, u'Reprueba')
	)
	resultados_condicion = models.CharField(max_length=30, choices=resultadoCondicion_choices, blank=False)

	class Meta:
		ordering = ('fecha_post',)
		verbose_name= 'Postulacion'
		verbose_name_plural = 'Postulaciones'

	def __str__(self):
		return self.alumno.nombre


	def to_dict_json(self):
		return {
			'id': self.id,
			'fecha_post': self.fecha_post,
			'universidad_procedencia': self.universidad_procedencia,
			'nivelacion': self.get_nivelacion_display(),
			'semestre_ingreso': self.semestre_ingreso,
			'anio_ingreso': self.anio_ingreso,
			'estado_matricula': self.get_estado_matricula_display(),
			'antecedentes_academicos': self.antecedentes_academicos,
			'antecedentes_profesionales': self.antecedentes_profesionales,
			'carta_recomendacion': self.carta_recomendacion,
			'entrevista': self.entrevista,
			'puntaje': self.puntaje,
			'resultados_condicion': self.get_resultados_condicion_display(),
		}


class Pagos(models.Model):
	alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	id_pago = models.BigAutoField(null=False, primary_key=True) #PORQUE CUANDO ELIMINAMOS UNO SE BORRA DEL REGISTRO EN LAS LISTAS. EL BIGAUTOFIELD SUPLE EL QUE SE BORRA Y AUTOMATICAMENTE SE ACTUALIZA PARA MANTENER LA SECUENCIA NUMERICA
	fecha_pag = models.DateField(null=False)
	monto = models.IntegerField(null=False)
	transferencia = 'Transferencia'
	efectivo = 'Efectivo'
	cheque = 'Cheque'
	credito = 'Credito'
	debito = 'Debito'
	tipo_pago_choices = (
		(transferencia, u'Transferencia'),
		(efectivo, u'Efectivo'),
		(cheque, u'Cheque'),
		(credito, u'Credito'),
		(debito, u'Debito'),
	)
	tipo_pago = models.CharField(max_length=30, choices=tipo_pago_choices, blank=False, null=False)
	banco = models.CharField(max_length=50, null=True)

	class Meta:
		ordering = ('fecha_pag', 'alumno')
		verbose_name= 'Pago'
		verbose_name_plural = 'Pagos'

	def __str__(self):
		return self.alumno.nombre + " " + self.alumno.apellido_pat + " " + self.alumno.apellido_mat 


	def to_dict_json(self):
		return {
			'id': self.id,
			'id_pago': self.id_pago,
			'fecha_pag': self.fecha_pag,
			'monto': self.monto,
			'tipo_pago': self.get_tipo_pago_display(),
			'banco': self.banco,
		}

class DireccionAlumno(models.Model):
	alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)
	provincia = GroupedForeignKey(Provincia, 'region')
	comuna = GroupedForeignKey(Comuna, 'provincia')
	direccion = models.CharField(max_length=300, null=True)

	class Meta:
		ordering = ('region', 'provincia', 'comuna')
		verbose_name='Direccion_alumno'
		verbose_name_plural = 'Direcciones_alumnos'


	def __str__(self):
		cadena = self.region.nombre+", "+self.comuna.nombre+"("+self.alumno.nombre+" "+self.alumno.apellido_pat+" "+self.alumno.apellido_mat+")"
		return cadena


	def to_dict_json(self):
		return {
			'id': self.id,
			'alumno_id': self.alumno_id,
			'region_id': self.region_id,
			'provincia_id': self.provincia_id,
			'comuna_id': self.comuna_id,
			'direccion': self.direccion,
		}


class Mensualidad(models.Model):
	monto = models.IntegerField(null=True, blank=True)

class Matricula(models.Model):
	monto = models.IntegerField(null=True, blank=True)

class Cobros(models.Model):
	alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	mensualidad = models.ForeignKey(Mensualidad, null=True, blank=True, on_delete=models.CASCADE)
	matricula = models.ForeignKey(Matricula, null=True, blank=True, on_delete=models.CASCADE)
	derecho_inscripcion = models.BooleanField(null=True, blank=True, default=True)
	id_cobro = models.BigAutoField(null=False, primary_key=True)
	mensualidad = models.IntegerField(null=True, blank=True)
	pagado = 'Pagado'
	vencido = 'Vencido'
	pendiente = 'Pendiente'
	estado_opciones = (
		(pagado, u'Pagado'),
		(vencido, u'Vencido'),
		(pendiente, u'Pendiente')
	)
	estado = models.CharField(max_length=30, choices=estado_opciones, blank=False, null=False)
	fecha_emision = models.DateField(null=False, blank=False)
	fecha_vencimiento = models.DateField(null=False, blank=False)
	monto = models.IntegerField(blank=False, null=False)


#MODELO DE APP PROGRAMA QUE CONTIENE DATOS DE ALUMNOS

class Programa(models.Model):
	alumno = models.ForeignKey(Alumno, null=True, blank=True, on_delete=models.CASCADE)
	monto = models.IntegerField(null=False, blank=False)
	semestre = models.IntegerField(null=False, blank=False)
	anio = models.CharField(max_length=4, null=False, blank=False)
	semestral = 'Semestral'
	trimestre = 'Trimestre'
	opciones = (
		(semestral, u'Semestral'),
		(trimestre, u'Trimestre')
	)
	modalidad = models.CharField(max_length=50, choices=opciones, null=True, blank=True)
	descripcion = models.CharField(max_length=300, null=True, blank=True)
















#MODELOS DE PROCESO DE TITULACIÓN DEL LUCHO. COMIENZAN ACÁ, SE HARÍA OTRA APP PERO PROFESOR Y ALUMNO
#SE IMPORTAN EN OTRAS APPS



