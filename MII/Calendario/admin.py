from django.contrib import admin
from Calendario.models import Tarea, EstadoTarea, TipoTarea, Edificio, Sala

# Register your models here.
admin.site.register(Tarea)
admin.site.register(EstadoTarea)
admin.site.register(TipoTarea)
admin.site.register(Edificio)
admin.site.register(Sala)