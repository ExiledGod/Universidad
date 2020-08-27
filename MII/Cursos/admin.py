from django.contrib import admin
from Cursos.models import Cursos, Detalle_curso, AvanceCurricular, semestre1, semestre2, semestre3, trimestral

admin.site.register(Cursos)
admin.site.register(Detalle_curso)
admin.site.register(AvanceCurricular)
admin.site.register(semestre1)
admin.site.register(semestre2)
admin.site.register(semestre3)
admin.site.register(trimestral)
