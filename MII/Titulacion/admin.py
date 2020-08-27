from django.contrib import admin
from Titulacion.models import profeExaminador, comite, estado, detalle, entrega, Alumno_en_Titulacion, Titulacion, enviar_email, inscripcion_tema
# Register your models here.

admin.site.register(Titulacion)
admin.site.register(Alumno_en_Titulacion)
admin.site.register(comite)
admin.site.register(profeExaminador)
admin.site.register(detalle)
admin.site.register(estado)
admin.site.register(entrega)
admin.site.register(enviar_email)
admin.site.register(inscripcion_tema)