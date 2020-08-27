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
from Profesor.models import Profesor, Tipo_grado, DireccionProfesor

router = routers.DefaultRouter()


urlpatterns = [
    path('registroProfesor', views.registroProfesor.as_view(), name='registroProfesor'),
    path('tipoGrado', views.tipoGrado, name='tipoGrado'),
    path('lista_profesores', views.profesorList.as_view(), name='profesorList'),
    path('ficha_docente/<int:pk>', views.ficha_docente, name='ficha_docente'),
    path('agregar_grado/<int:pk>', views.agregar_grado, name='agregar_grado'),
    path('datos_direccion_profesor/<int:pk>', views.direccionListProfesor.as_view(), name='datos_direccion'),
    path('editar_direccion_profesor/<int:pk>', views.direccionListEditarProfesor, name='editar_direccion'),
    url(r'^busqueda_ficha_docente/$', views.busqueda_ficha_docente, name='busqueda_ficha_docente'),
    path('cursos_dictados/<int:pk>', views.cursos_dictados, name='cursos_dictados'),
    path('eliminar_profesor/<int:pk>', views.eliminar_profesor.as_view(), name='eliminar_profesor'),
    path('eliminar_detallecurso/<int:pk>', views.eliminar_detallecurso.as_view(), name='eliminar_detallecurso'),
    path('agregar_detallecurso/<int:pk>', views.agregar_detallecurso.as_view(), name='agregar_detallecurso'),

    #-------------URL DE MANTENEDORES------------
    path('mantenedor/docente/<int:pk>', views.mantenedor_docentes_home, name='docentes_home'),
]

