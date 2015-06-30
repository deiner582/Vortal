from django.conf.urls import patterns ,url

urlpatterns = patterns('',
   url(r'^pensum/', 'Admin.views.pensum', name='pensum'),
)
