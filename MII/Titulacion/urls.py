from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from rest_framework import routers, serializers, viewsets, generics

router = routers.DefaultRouter()

urlpatterns = [
    path('Titulacion', views.plantilla_principal_t, name='titulacion'),
    path('Agregar_titulacion', views.agregar_titulacion.as_view(), name='listado_titulacion'),
    path('Enviar_correos', views.enviar_correos, name='correos'),
    path('test',views.prueba,name='Prueba'),
	path('Form_Examinador', views.profeExaminadorViews.as_view(), name='Examinador'),
	path('agregar_Estado', views.estadoViews.as_view(), name='Estado'),
    path('agregar_Entrega', views.entregaViews.as_view(), name='Entrega'),
    path('agregar_titulacion', views.crear_titulacion.as_view(), name='crear_titulacion'),
    path('alumnos_en_titulacion', views.listado_alumnos_en_titulacion, name='listado_alumnos_en_titulacion'),
    path('estado_actual/<int:pk>', views.estado_actual, name='estado_actual'),
    path('seguimiento/<int:pk>', views.proceso_seguimiento, name='proceso'),
    path('enviar_correo/<int:pk>', views.enviar_correo, name='enviar_correo'),
    path('mensaje_enviado/<int:pk>', views.mensaje_enviado_exitosamente, name='mensaje_enviado'),
    path('inscripcion_tema/<int:pk>', views.agregar_inscripcion, name='inscripcion_tema'),
    path('primera_entrega/<int:pk>', views.primera_entrega, name='primera_entrega'),
    path('agregar_primera_entrega/<int:pk>', views.agregar_primera_entrega, name='agregar_primera_entrega'),
]