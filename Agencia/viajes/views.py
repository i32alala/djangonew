from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.views.generic import TemplateView,RedirectView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

class LoginUser(FormView):
    model = User
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return render(request, self.get_success_url())
        else:
            return super(LoginUser, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect(self.get_success_url())

class LogoutUser(RedirectView):
    url = reverse_lazy('index')
    settings.LOGIN_URL = '/login/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LogoutUser, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutUser, self).get(request, *args, **kwargs)

def verDestino(request):
	dest = Destino.objects.all()
	context = {'destinos':dest}
	return render(request,'verDestinos.html',context)

def anadirDestino(request):
	if request.method == 'POST':
		dest = Destino()
		formulario = DestinoForm (request.POST, instance = dest)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = DestinoForm()
	return render_to_response('anadirDestinos.html',{'formulario':formulario}, context_instance = RequestContext(request))
	
def detalleDestino(request, destino_id):
	dest = Destino.objects.get(pk= destino_id)
	context = {'destinoDetalle':dest}
	return render(request, 'detalleDestino.html',context)

def modificarDetinoMostrar(request):
	dest = Destino.objects.all()
	context = {'destinos':dest}
	return render(request,'modificarDestMos.html',context)
	
def modificarDestino(request, destino_id):
	dest = Destino.objects.get(id = destino_id)
	if request.method == 'POST':
		formulario = DestinoForm(request.POST, instance = dest)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = DestinoForm(instance = dest)
	context = {'formulario':formulario}
	return render_to_response('modificarDestino.html',context,context_instance=RequestContext(request))

def borrarDestino(request, destino_id):
	dest = Destino.objects.get(id=destino_id).delete()
	context={'destinos':dest}
	return redirect('/destinos/verDestino')
	
def verPaquete(request):
	paq = Paquete.objects.all()
	context = {'paquetes':paq}
	return render(request,'verPaquete.html',context)
	
def paqueteDetalle(request, paquete_id):
	paq = Paquete.objects.get(pk = paquete_id)
	context = {'paqueteDetalle':paq}
	return render(request,'detallePaquete.html',context)

def anadirPaquete(request):
	if request.method == 'POST':
		paq = Paquete()
		formulario = paqueteForm (request.POST, instance = paq)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = paqueteForm()
	return render_to_response('anadirPaquete.html',{'formulario':formulario}, context_instance = RequestContext(request))
	
class verRuta(View):
	template_name ='verRuta.html'
	def get(self, request,*args, **kwargs):
		rutas = Ruta.objects.all()
		return render(request,self.template_name, {'rutas':rutas})

class detalleRuta(View):
	template_name= 'detalleRuta.html'
	
	def get(self,request, *arg, **kwargs):
		id = self.kwargs['Ruta_id']
		ruta = get_object_or_404(Ruta, pk=id)
		return render(request,self.template_name,{'rutaDetalle':ruta,'user':request.user})


