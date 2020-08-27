from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from braces.views import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView, TemplateView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import render_to_response
import request
from django.db.models import Q

from Alumno.forms import AlumnoForm
from Alumno.models import Alumno
from Cursos.models import AvanceCurricular
from Titulacion.models import profeExaminador,comite,estado,detalle,entrega,Alumno_en_Titulacion,Titulacion, enviar_email
from Titulacion.models import inscripcion_tema
from Titulacion.forms import inscripcion_tema_form
from Titulacion.forms import profeExaminadorForm,estadoForm,entregaForm,AlumnoTitulacionForm,titulacionForm, enviar_email_form
# Create your views here.

@login_required()
def plantilla_principal_t(request):
	return render(request, 'Titulacion/titulacion_principal.html')

@login_required()
def enviar_correos(request):
	return render(request, 'Titulacion/enviar_correos.html')

def prueba(request):
	return render(request,'Test/test.html')

class agregar_titulacion(LoginRequiredMixin, ListView):
	model = AvanceCurricular
	template_name = 'Titulacion/agregar_titulacion_listado.html'
	form_class = AlumnoForm
	success_url = reverse_lazy('listado_titulacion')
	paginate_by = 10


class profeExaminadorViews(LoginRequiredMixin, CreateView):
    model = profeExaminador
    template_name = 'Titulacion/ExaminadorForm.html'
    form_class = profeExaminadorForm
    success_url = reverse_lazy('Examinador')


class crear_titulacion(SuccessMessageMixin, LoginRequiredMixin, CreateView):
	model = Titulacion
	template_name = 'Titulacion/agregar_titulacion.html'
	form_class = titulacionForm
	success_url = reverse_lazy('listado_alumnos_en_titulacion')


class estadoViews(LoginRequiredMixin, CreateView):
    model = estado
    template_name = 'Titulacion/estadoForm.html'
    form_class = estadoForm
    success_url = reverse_lazy('Estado')
    paginate_by = 10

class entregaViews(LoginRequiredMixin, CreateView):
    model = entrega
    template_name = 'Titulacion/entregaForm.html'
    form_class = entregaForm
    success_url = reverse_lazy('Entrega')
    paginate_by = 10

@login_required()
def listado_alumnos_en_titulacion(request):
    alumno = Alumno_en_Titulacion.objects.all()

    return render(request, 'Titulacion/listado_alumnos_en_titulacion.html', {'alumno': alumno})

@login_required()
def estado_actual(request, pk):
    alumno = Alumno_en_Titulacion.objects.filter(id=pk)

    return render(request, 'Titulacion/estado_actual.html', {'alumno': alumno})

@login_required()
def proceso_seguimiento(request, pk):
    alumno = Alumno_en_Titulacion.objects.filter(id=pk)

    return render(request, 'Titulacion/proceso.html', {'alumno': alumno})


@login_required()
def mensaje_enviado_exitosamente(request, pk):
    alumno = Alumno_en_Titulacion.objects.filter(id=pk)

    return render(request, 'Titulacion/correo_enviado.html', {'alumno': alumno})


@login_required()
def enviar_correo(request, pk):
    alumno = Alumno_en_Titulacion.objects.get(id=pk)
    body = render_to_string(
        'Titulacion/email_content.html',{
            'nombre': alumno.nombre,
            'apellido_p': alumno.apellido_pat,
            'apellido_m': alumno.apellido_mat,
            'email': alumno.mail,
        },
    )

    email_message = EmailMessage(
        subject ='Información Titulación Programa Magíster',
        body = body,
        from_email = 'info.mii.pucv@gmail.com',
        to=[alumno.mail],
    )
    email_message.content_subtype = 'html'
    email_message.send()

    return render(request, 'Titulacion/correo_enviado.html', {'alumno': alumno})


@login_required()
def primera_entrega(request, pk):
    alumno = Alumno_en_Titulacion.objects.filter(id=pk)

    return render(request, 'Titulacion/primera_entrega.html', {'alumno': alumno})


@login_required()
def agregar_inscripcion(request, pk):
    alumno = get_object_or_404(Alumno_en_Titulacion, pk=pk)
    inscripcion = inscripcion_tema_form(request.POST or None)
    if inscripcion.is_valid():
        agregar_inscripcion = inscripcion.save(commit=False) #todavía no lo guardo
        agregar_inscripcion.alumno = alumno #le agrego el id del alumno
        agregar_inscripcion.save() #lo guardo
        messages.success(request, 'Se han agregado correctamente los datos de inscripcion')
        return redirect('primera_entrega', pk)

    return render(request, 'Titulacion/inscripcion_tema.html', {'form': inscripcion})

@login_required()
def agregar_primera_entrega(request, pk):
    alumno = get_object_or_404(Alumno_en_Titulacion, pk=pk)
    primera_entrega = entregaForm(request.POST or None)
    if primera_entrega.is_valid():
        agregar_primera_entrega = primera_entrega.save(commit=False) #todavía no lo guardo
        agregar_primera_entrega.alumno = alumno #le agrego el id del alumno
        agregar_primera_entrega.save() #lo guardo
        messages.success(request, 'Se han agregado correctamente los datos de inscripcion')
        #return redirect('agregar_primera_entrega', pk)

    return render(request, 'Titulacion/agregar_primera_entrega.html', {'form': primera_entrega})