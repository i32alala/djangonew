from django.forms import ModelForm
from django import forms
from .models import * 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DestinoForm(forms.ModelForm):
	class Meta:
		model = Destino

class paqueteForm(forms.ModelForm):
	class Meta:
		model = Paquete

class UserForm(django.forms.ModelForm):
    class Meta:
        model = User  

class UserProfileForm(django.forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
