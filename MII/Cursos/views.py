from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from braces.views import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView, TemplateView
from .forms import Detalle_curso_form, Lista_alumnos_form, Cursos_form, Avance_form, Malla_curricular_form
from .models import Lista_alumnos, Detalle_curso, Cursos, AvanceCurricular, Malla_curricular
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from Profesor.models import Profesor
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Alumno.models import Alumno, Postulacion


class agregar_curso(SuccessMessageMixin, LoginRequiredMixin, CreateView):
	model = Cursos
	template_name = 'Cursos/agregar_curso.html'
	form_class = Cursos_form
	success_url = reverse_lazy('registroCurso')
	success_message = "El curso fue creado satisfactoriamente"

class cursos_en_malla(LoginRequiredMixin, CreateView):
	model = Cursos
	template_name = 'Cursos/cursos_en_malla.html'
	form_class = Cursos_form
	success_url = reverse_lazy('cursos_en_malla')

class eliminar_curso(LoginRequiredMixin, DeleteView):
	model = Cursos
	template_name = 'Cursos/eliminar_curso.html'
	form_class = Cursos_form
	success_url = reverse_lazy('mantenedor_curso')

@login_required()
def obligatorios_optativos(request, pk):
	model = Cursos
	cursos = Cursos.objects.get(id=pk)
	if cursos.tipo == 'Obligatorio':
		return render(request, 'Cursos/cursos_obligatorios.html', {'cursos': cursos})
	else:
		return render(request, 'Cursos/cursos_optativos.html', {'cursos': cursos})
	return render (request, 'Cursos/cursos_en_malla.html')


# CLASE QUE MUESTRA CURSOS HISTORICOS EN PLANTILLA DE BUSQUEDA
#class historicos(LoginRequiredMixin, ListView):
	#model = Detalle_curso
	#template_name = 'Cursos/historicos.html'
	#form_class = Detalle_curso_form
	#success_url = reverse_lazy('historicos')


# FUNCIÓN QUE MUESTRA LOS CURSOS EN PLANTILLA DE BÚSQUEDA
@login_required()
def historicos(request):
	context = {}
	lista_detalle = Detalle_curso.objects.all()
	paginator = Paginator(lista_detalle, 5)
	context['lista_detalle']= lista_detalle
	return render (request, 'Cursos/historicos.html', context)


@login_required()
def detalle_curso(request, pk):
	curso = Detalle_curso.objects.get(curso_id=pk)


	return render(request, 'Cursos/detalle_curso.html', {'curso': curso})



@login_required()
def avance_curricular(request, pk):
	avance = AvanceCurricular.objects.filter(alumno_id=pk) #se usa filter por coincidencias del M2M, replicará x veces encontrado el resultado
	alumno = Alumno.objects.filter(id=pk)
	postulacion = Postulacion.objects.filter(alumno_id=pk)
	return render(request, 'Alumno/avance_curricular.html', {'avance': avance, 'alumno': alumno, 'postulacion': postulacion})


class AvanceLista(LoginRequiredMixin, ListView):
	model = AvanceCurricular
	template_name = 'Alumno/avance_curricular.html'
	success_url = reverse_lazy('avance_curricular')


class malla_antigua(LoginRequiredMixin, ListView):
	model = Cursos
	form_class = Cursos_form
	template_name = 'Cursos/malla_antigua.html'
	success_url = reverse_lazy('malla_curricular_antigua')
	

class malla_nueva(LoginRequiredMixin, ListView):
	model = Cursos
	form_class = Cursos_form
	template_name = 'Cursos/malla_nueva.html'
	success_url = reverse_lazy('malla_curricular_nueva')

class crear_detalle_curso(SuccessMessageMixin, LoginRequiredMixin, CreateView):
	model = Detalle_curso
	form_class = Detalle_curso_form
	template_name = 'Cursos/agregar_detalle_curso.html'
	success_url = reverse_lazy('agregar_detalle_curso')
	success_message = "Se ha agregado un Registro de Curso Exitosamente"

#FUNCIONES DE MANTENEDORES

@login_required()
def mantenedor_cursos_home(request, pk):
	objeto = Cursos.objects.filter(id=pk)

	return render(request, 'Mantenedores/cursos_home.html', {'curso': objeto})