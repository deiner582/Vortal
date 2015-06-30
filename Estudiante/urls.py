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
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^principal/(?P<pk>.*)$', Logueado.as_view(), name='home'),
    url(r'^horario/(?P<pk>.*)$',HorarioView.as_view(), name='opcion'),
    url(r'^pensum/(?P<pk>.*)-(?P<pr>\w+)$',pensum.as_view(), name='pensum'),
    url(r'^matricula/(?P<pk>.*)$',ListaMateriasGrupos.as_view(), name='Detalle'),
    url(r'^matriculamateria/(?P<pk>.*)$',ListaGrupos.as_view(), name='matriculamateria'),
    url(r'^financiera/(?P<pk>.*)$', MatriculaFinancier.as_view(), name='opcion'),
    url(r'^lista/', ListaEstudiante.as_view(), name='lista'),
    url(r'^hoja/(?P<pk>.*)$',DetalleEstudiante.as_view(), name='Detalle'),
    url(r'^crear/', CrearEstudiante.as_view(), name='Crear'),
    url(r'^eliminar/(?P<pk>.*)$', ElimnarFacultad.as_view(), name='eliminar'),
    url(r'^editar/(?P<pk>.*)$', ActulizarFacultad.as_view(), name='actualizar'),
    url(r'^registrarestudiante/', RegistroEstudiante.as_view(), name='registrar_estudiante'),
    url(r'^horario-(?P<pk>.*)-(?P<gr>\w+)-((?P<cod>\w+)/)?$',HorarioGrupo.as_view(), name='Horario'),
    url(r'^matricular-(?P<pk>.*)-(?P<gr>\w+)-((?P<cod>\w+)/)?$',MatricularMateria.as_view(), name='matricula'),
    url(r'^eliminar-(?P<pk>.*)-(?P<gr>\w+)-((?P<cod>\w+)/)?$',EliminarMateria.as_view(), name='eliminarmateria'),
    url(r'^opcion/(?P<pk>.*)$',Opcion.as_view(), name='opcioncalificacion'),
    url(r'^notas/(?P<pk>.*)$',Notas.as_view(), name='notas'),
]
