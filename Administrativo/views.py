from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from .models import Facultad
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class CrearFacultad(CreateView):
    model = Facultad
    success_url = '/'
    template_name = 'facultad.html'
    fields = ['nombre']






