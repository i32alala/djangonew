from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from viajes import views
from viajes.views import LoginUser,LogoutUser


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Agencia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', TemplateView.as_view(template_name='content.html'), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', LoginUser.as_view(), name ='Login'),
    url(r'^logout', LogoutUser.as_view(), name='Logout'),
    url(r'^destinos',include('viajes.urls'), name='destinos'),
    url(r'^paquetes',include('viajes.urls'), name='paquetes'),
    url(r'^rutas',include('viajes.urls'), name='rutas'),
)
