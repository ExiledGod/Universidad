from Calendario.models import Tarea, TipoTarea, EstadoTarea
from django  import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
        }

class TareaUpdateForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            'titulo',
            'descripcion',
            'fechaTermino',
            'estadoTarea',
        ]
        labels = {
            'titulo': 'Titulo',
            'descripcion': 'Descripcion',
            'fechaTermino': 'Fecha de termino',
            'estadoTarea': 'Estado de la tarea',
        }