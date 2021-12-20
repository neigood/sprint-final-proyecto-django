from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Caso, Contacto
from django.db import models
from django.db.models import fields


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CasoForm(forms.ModelForm):
    class Meta:
        model = Caso
        fields = ("tu_nombre", "tu_opinion")


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        # fields = '__alll__'  # incluye todo los campos de la clase
