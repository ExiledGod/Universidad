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
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from rest_framework import routers, serializers, viewsets, generics

router = routers.DefaultRouter()

urlpatterns = [
    path('tareas', views.tareas, name='tareas'),
    path('creartarea', views.crear_tarea, name='crear_tarea'),
    path('<int:pk>', views.TareaDelete.as_view(), name='eliminar_tarea'),
    #path('register', views.RegistroUsuario.as_view(), name='register'),
    #path('editar_tarea/<int:pk>', views.TareaUpdate.as_view(), name='editar_tarea'),
    path('editartarea/<int:pk>', views.actualizarTarea, name='editar_tarea'),
    path('calendario', views.calendario, name='calendario'),
    path('detallestarea/<int:pk>', views.TareaDetail.as_view(), name='detalles_tarea'),
]