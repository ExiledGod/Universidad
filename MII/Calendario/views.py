from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import User
from Calendario.models import Tarea, EstadoTarea, TipoTarea, Edificio, Sala
from .forms import RegistroForm, TareaUpdateForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
import time

#decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required, name='get')
class TareaUpdate(UpdateView):
    model = Tarea
    form_class = TareaUpdateForm
    template_name = 'Calendario/editar_tarea.html'
    success_url = reverse_lazy('tareas')

@method_decorator(login_required, name='get')
class TareaDelete(DeleteView):
    model = Tarea
    template_name = 'Calendario/confirm_delete.html'
    success_url = reverse_lazy('tareas')
    
@method_decorator(login_required, name='get')
class TareaDetail(DetailView):
    model = Tarea
    template_name = 'Calendario/detalles_tarea.html'

@login_required()
def calendario(request):
    tareas = Tarea.objects.all()
    return render(request, "Calendario/calendario.html", { 'tareas' : tareas })

@login_required()
def tareas(request):
    if User.is_staff:
        tareas = Tarea.objects.all()
        estadoTarea = EstadoTarea.objects.all()
        tipoTarea = TipoTarea.objects.all()
        edificio = Edificio.objects.all()
        sala = Sala.objects.all()
        context = {'tareas' : tareas, 'estadoTarea' : estadoTarea, 'tipoTarea': tipoTarea, 'edificio': edificio, 'sala': sala}
    else:
        
        tareas = Tarea.objects.filter(usuario=request.user)
        estadoTarea = EstadoTarea.objects.all()
        tipoTarea = TipoTarea.objects.all()
        edificio = Edificio.objects.all()
        sala = Sala.objects.all()
        context = {'tareas' : tareas, 'estadoTarea' : estadoTarea, 'tipoTarea': tipoTarea, 'edificio': edificio, 'sala': sala}
    # tareas = Tarea.objects.all()
    return render(request, 'Calendario/tareas.html', context=context)

@login_required()
def crear_tarea(request):
    if request.method == 'POST':
        tarea = Tarea()
        tarea.titulo = request.POST.get('titulo_tarea')
        tarea.descripcion = request.POST.get('descripcion_tarea')
        tarea.usuario = request.user
        tarea.fechaInicio = time.strftime("%Y-%m-%d")
        tarea.fechaTermino = request.POST.get('fechaTermino')
        tarea.edificio = Edificio.objects.get(pk=request.POST.get('Edificio'))
        tarea.sala= Sala.objects.get(pk=request.POST.get('Sala'))
        tarea.estadoTarea = EstadoTarea.objects.get(pk=request.POST.get('estadoT'))
        tarea.tipoTarea = TipoTarea.objects.get(pk=request.POST.get('tipoTarea'))
        tarea.save()
    return redirect('tareas')

@login_required()
def actualizarTarea(request, pk):
    tarea = Tarea.objects.get(pk=pk)
    if request.method == 'GET':
        form = TareaUpdateForm(instance=tarea)
    else:
        form = TareaUpdateForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
        return redirect('tareas')
    return render(request, 'Calendario/editar_tarea.html', {'form':form})