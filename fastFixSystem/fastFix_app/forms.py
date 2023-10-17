# forms.py
from django import forms
from .models import Cliente
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class RegistroClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'correo', 'contraseña']

