from django.conf.urls import patterns, include, url
from django.contrib import admin
from Admin.views import Index,Logueado
import debug_toolbar
urlpatterns = patterns('',
    # Examp
    # les:
     #url(r'^principal/(?P<ced>.*)$', 'Admin.views.hojadevida',name='hoja'),
   url(r'^pensum/', 'Admin.views.pensum', name='pensum'),
)
