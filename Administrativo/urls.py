from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examp
    # les:
     #url(r'^principal/(?P<ced>.*)$', 'Admin.views.hojadevida',name='hoja'),
   url(r'^pensum/', 'Admin.views.pensum', name='pensum'),
)
