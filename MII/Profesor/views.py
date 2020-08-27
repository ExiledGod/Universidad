from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from braces.views import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from .forms import ProfesorForm, Tipo_gradoForm, DireccionProfesorForm, ProfesorGradoForm
from .models import Profesor, Tipo_grado, DireccionProfesor
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import render_to_response
import request
from django.db.models import Q
from Cursos.models import Detalle_curso
from Cursos.forms import Detalle_curso_form


# Create your views here.

def tipoGrado(request):
    return render(request, 'Profesor/tipo_grado.html', {})

class registroProfesor(LoginRequiredMixin, CreateView):
    form_class = ProfesorGradoForm
    template_name = 'Profesor/registro_profesor.html'
    success_url = reverse_lazy('registroProfesor')

class profesorList(LoginRequiredMixin, ListView):
	model = Profesor
	template_name = 'Profesor/profesorList.html'
	form_class = ProfesorForm
	success_url = reverse_lazy('profesorList')
	paginate_by = 10

@login_required()
def ficha_docente(request, pk):
	objeto1 = Profesor.objects.filter(id=pk)
	objeto2 = DireccionProfesor.objects.filter(profesor_id=pk)
	objeto3 = Tipo_grado.objects.filter(profesor_id=pk)

	return render(request, 'Profesor/ficha_docente.html', {'profesor': objeto1, 'direccion': objeto2, 'grado': objeto3})


@login_required()
def agregar_grado(request, pk):
	profesor = get_object_or_404(Profesor, pk=pk)
	grado = Tipo_gradoForm(request.POST or None)
	if grado.is_valid():
		nuevo_grado = grado.save(commit=False) #todavía no lo guardo
		nuevo_grado.profesor = profesor #le agrego el id del profesor
		nuevo_grado.save() #lo guardo
		messages.success(request, 'Se ha agregado correctamente')
		return redirect('ficha_docente', pk)

	return render(request, 'Profesor/agregar_grado.html', {'form': grado})


class direccionListProfesor(LoginRequiredMixin, UpdateView):
    model = DireccionProfesor
    template_name = 'Profesor/datos_direccion.html'
    form_class = DireccionProfesorForm
    success_url = reverse_lazy('lista_profesores')

@login_required()
def direccionListEditarProfesor(request, pk):
    direccion = DireccionProfesor.objects.get(profesor_id=pk)
    if request.method == 'GET':
        form = DireccionProfesorForm(instance=direccion)
    else:
        form = DireccionProfesorForm(request.POST, instance=direccion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha editado la información correctamente')
        return redirect('datos_direccion', pk)
    return render(request, 'Profesor/editar_direccion.html', {'form':form})


#FUNCIÓN QUE REALIZA BÚSQUEDA EN PLANTILLA DE 'VER FICHA ACADÉMICA'
 
@login_required()
def busqueda_ficha_docente(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__icontains=query) | 
            Q(rut__icontains=query) |
            Q(mail__icontains=query)
        )
        results = Profesor.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('Profesor/busqueda_ficha.html', {'results': results, 'query': query})


@login_required()
def cursos_dictados(request, pk):
    cursos = Detalle_curso.objects.filter(profesor_id=pk)
    profesor = Profesor.objects.filter(id=pk)
    return render(request, 'Cursos/cursos_dictados.html', {'cursos':cursos, 'profesor': profesor})


#FUNCIONES DE MANTENEDORES

@login_required()
def mantenedor_docentes_home(request,pk):
    objeto1 = Profesor.objects.filter(id=pk)
    objeto2 = DireccionProfesor.objects.filter(profesor_id=pk)
    objeto3 = Tipo_grado.objects.filter(profesor_id=pk)
    objeto4 = Detalle_curso.objects.filter(profesor_id=pk)

    return render(request, 'Mantenedores/docente_home.html', {'profesor': objeto1, 'direccion': objeto2, 'grado': objeto3, 'detallecurso': objeto4})

class eliminar_profesor(LoginRequiredMixin, DeleteView):
    model = Profesor
    template_name = 'Profesor/eliminar_docente.html'
    form_class = ProfesorForm
    success_url = reverse_lazy('mantenedor_docente')

class eliminar_detallecurso(LoginRequiredMixin, DeleteView):
    model = Detalle_curso
    template_name = 'Profesor/eliminar_detallecurso.html'
    form_class = Detalle_curso_form
    success_url = reverse_lazy('mantenedor_docente')

class agregar_detallecurso(LoginRequiredMixin, CreateView):
    model = Detalle_curso
    template_name = 'Profesor/agregar_detallecurso.html'
    form_class = Detalle_curso_form
    success_url = reverse_lazy('mantenedor_docente')