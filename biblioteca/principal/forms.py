from django import forms
from principal.models import Libro
from principal.models import Perfiles
from principal.models import Prestamo
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from django.utils import timezone 


"""class  usuarioform(forms.ModelForm):
	class Meta:
		model= Usuario"""


class  prestamoform(forms.ModelForm):
	class Meta:
		model= Prestamo
  


class UserForm(UserCreationForm):
	nombre = forms.CharField(max_length=50)
	apellidos = forms.CharField(max_length=50)
	direccion= forms.CharField(max_length=120)
	telefono = forms.CharField(max_length=9)


class ContactoForm(forms.Form):
	Correo_Usuario = forms.EmailField(label='TU CORREO ELECTRONICO')
	mensaje = forms.CharField(widget=forms.Textarea)


		