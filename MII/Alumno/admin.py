from django.contrib import admin
from Alumno.models import Alumno, Postulacion, Cursos_homologados, Pagos, Becas, DireccionAlumno, Programa, Cobros
from Alumno.models import Mensualidad, Matricula

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Postulacion)
admin.site.register(Pagos)
admin.site.register(Cobros)
admin.site.register(Becas)
admin.site.register(DireccionAlumno)
admin.site.register(Programa)
admin.site.register(Mensualidad)
admin.site.register(Matricula)
