from django.conf.urls import patterns, include, url
from django.contrib import admin
from Admin.views import Index,Logueado
import debug_toolbar
urlpatterns = patterns('',
    # Examp
    # les:
     #url(r'^principal/(?P<ced>.*)$', 'Admin.views.hojadevida',name='hoja'),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^hoja/', 'Admin.views.hojadevida',name='hoja'),
     url(r'^$', Index.as_view(), name='index'),
     url(r'^principal/', Logueado.as_view(), name='home'),
     url(r'^pensum/', 'Admin.views.pensum', name='pensum'),
     url(r'^opcion/', 'Admin.views.opcioncalificacion', name='opcion'),
     url(r'^matricula/', 'Admin.views.matricula', name='opcion'),
     url(r'^matriculamateria/', 'Admin.views.matriculamateria', name='opcion'),
    url(r'^horario/', 'Admin.views.horario', name='opcion'),
    url(r'^financiera/', 'Admin.views.financiera', name='opcion'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
