from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

# Create your models here

# Un destino es un lugar al que se puede viajar, pero sin incluir los datos respecto al viaje, como precio, etc...
class Destino(models.Model):
	lugar = models.CharField(max_length=100)
	descripcion = models.TextField()
	distancia = models.IntegerField()
	
	def __unicode__(self):
        	return self.lugar

class Paquete(models.Model):
	contenido = models.CharField(max_length=100)
	valor = models.CharField(max_length=100)
	destinatario = models.ForeignKey(Destino)
	
	def __unicode__(self):
		return self.contenido
	
class Ruta(models.Model):
	nombre = models.CharField(max_length=100)
	paquetes = models.ManyToManyField(Paquete)
	
	def __unicode__(self):
		return self.nombre

