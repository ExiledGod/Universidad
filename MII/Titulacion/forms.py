from django import forms
from django.forms.widgets import Select, SelectMultiple, Media
from django.forms.models import ModelChoiceField, ModelMultipleChoiceField
from django.forms import ChoiceField
from smart_selects.widgets import ChainedSelect, ChainedSelectMultiple
from django.utils.encoding import force_text
from betterforms.multiform import MultiModelForm
from Titulacion.models import Alumno_en_Titulacion,comite,entrega,detalle,profeExaminador,Titulacion,estado, enviar_email, inscripcion_tema

class profeExaminadorForm(forms.ModelForm):
    class Meta:
        model = profeExaminador
        fields = [
            'nombre',
            'apellido_pat',
            'apellido_mat',
            'rut',
            'mail',
            'titulo',
        ]
        labels = {
            'nombre': 'Nombre:',
            'apellido_pat': 'Apellido Paterno:',
            'apellido_mat': 'Apellido Materno',
            'rut': 'Rut:',
            'mail': 'Correo electronico:',
            'titulo': 'Titulo:',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_pat': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_mat': forms.TextInput(attrs={'class':'form-control'}),
            'rut': forms.TextInput(attrs={'class':'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
        }

class estadoForm(forms.ModelForm):
    class Meta:
        model = estado
        fields = [
            'nombre',
            'fecha',
            'valido',
        ]
        labels = {
            'nombre':'Nombre:',
            'fecha':'Fecha:',
            'valido':'Valido:',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control'}),
            'valido': forms.Select(attrs={'class':'form-control'}),
        }

class entregaForm(forms.ModelForm):
    class Meta:
        model = entrega
        fields = [
            'alumno',
            'nombre',
            'fecha_entrega',
            'nota',
            'comentario',
            'archivo',
            'tipo',
        ]
        labels = {
            'alumno': 'Seleccione Alumno:',
            'nombre':'Nombre:',
            'fecha_entrega':'Fecha (D/M/A):',
            'nota':'Nota:',
            'comentario':'Comentarios (Opcional):',
            'archivo':'Archivo:',
            'tipo':'Seleccion tipo entrega:',
        }
        widgets = {
            'alumno': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control'}),
            'nota': forms.TextInput(attrs={'class':'form-control'}),
            'comentario': forms.TextInput(attrs={'class':'form-control'}),
            'archivo': forms.FileInput(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class':'form-control'}),
        }

class AlumnoTitulacionForm(forms.ModelForm):
    class Meta:
        model = Alumno_en_Titulacion
        fields = [
            'nombre',
            'apellido_pat',
            'apellido_mat',
            'rut',
            'mail',
        ]
        labels = {
            'nombre':'Nombre:',
            'apellido_pat':'Apellido Paterno:',
            'apellido_mat':'Apellido Materno:',
            'rut':'Rut:',
            'mail':'Correo Electronico:',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_pat': forms.TextInput(attrs={'class':'form-control'}),
			'apellido_mat': forms.TextInput(attrs={'class':'form-control'}),
			'rut': forms.TextInput(attrs={'class':'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class titulacionForm(forms.ModelForm):
    class Meta:
        model = Titulacion
        fields = [
            'alumno',
            'nombre_titulacion',
            'fecha',
        ]
        labels = {
            'alumno': 'Seleccione Alumnos:',
            'nombre_titulacion':'Periodo de Titulacion (ej. Titulación 2019S1):',
            'fecha':'Fecha de creación (D/M/A):',
        }
        widgets = {
            'alumno': forms.SelectMultiple(attrs={'class':'form-control'}),
            'nombre_titulacion': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.TextInput(attrs={'class':'form-control'}),
        }

class enviar_email_form(forms.ModelForm):
    class Meta:
        model = enviar_email
        fields = [
            'nombre',
            'email',
            'mensaje',
        ]
        labels = {
            'nombre': 'Ingrese su nombre:',
            'email': 'Ingrese email alumno:',
            'mensaje': 'Ingrese mensaje:',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
        }


class inscripcion_tema_form(forms.ModelForm):
    class Meta:
        model = inscripcion_tema
        fields = [
            'alumno',
            'profesor',
            'nombre_tema',
        ]
        labels = {
            'alumno': 'Seleccione Alumno:',
            'profesor': 'Seleccione Profesor Guía:',
            'nombre_tema': 'Nombre Tema:', 
        }
        widgets = {
            'alumno': forms.Select(attrs={'class': 'form-control'}),
            'profesor': forms.Select(attrs={'class': 'form-control'}),
            'nombre_tema': forms.TextInput(attrs={'class': 'form-control'}),
        }