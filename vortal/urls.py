"""vortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Estudiante.views import *
from Estudiante.views import Index,Logueado
urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^principal/', Logueado.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^horario/',HorarioView.as_view(), name='opcion'),
    url(r'^pensum/', 'Estudiante.views.pensum', name='pensum'),
     url(r'^opcion/', 'Estudiante.views.opcioncalificacion', name='opcion'),
     url(r'^matricula/', 'Estudiante.views.matricula', name='opcion'),
     url(r'^matriculamateria/', 'Estudiante.views.matriculamateria', name='opcion'),
    url(r'^financiera/', 'Estudiante.views.financiera', name='opcion'),
     url(r'^estudiante/(?P<ced>.*)$','Estudiante.views.Hojavida',name='Estudiante'),
      url(r'^lista/', ListaEstudiante.as_view(), name='lista'),
    url(r'^detalle/(?P<pk>.*)$',DetalleEstudiante.as_view(), name='Detalle'),
      url(r'^crear/', CrearEstudiante.as_view(), name='Crear'),
    url(r'^eliminar/(?P<pk>.*)$', ElimnarFacultad.as_view(), name='eliminar'),
    url(r'^editar/(?P<pk>.*)$', ActulizarFacultad.as_view(), name='actualizar'),
    url(r'^registrarestudiante/', RegistroEstudiante.as_view(), name='registrar_estudiante'),

]
