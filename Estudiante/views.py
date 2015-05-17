from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from django.template import RequestContext

from Administrativo.models import *
from .models import Estudiante
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,ListView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from Estudiante.forms import FormularioLogin

class Index(FormView):

    template_name = "index.html"
    form_class = FormularioLogin
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        usr = form.cleaned_data['usuario']
        psw = form.cleaned_data['contrasena']
        autenticacion = authenticate(username=usr, password=psw)
        if autenticacion is not None:
            print("Valido")
            if autenticacion.is_active:
                login(self.request,autenticacion)
                return redirect(reverse_lazy('home'))
            else:
                print("No Valido")
                return render_to_response('signin.html',{"estado":"Error de Usuario o Contrasena","form":form},context_instance=RequestContext(self.request))
        else:
            print("No Valido")
            return render_to_response('signin.html',{"estado":"Error de Usuario o Contrasena","form":form},context_instance=RequestContext(self.request))
        return super(Login, self).form_valid(form)

class Logueado(ListView):
    context_object_name = "estudiante"
    template_name = "home.html"

    def get_queryset(self):
        #self.publisher = get_object_or_404(Estudiante, name=self.args[0])
        contexto = Estudiante.objects.filter(usuario=self.request.user)
        return contexto

class HorarioView(TemplateView):
    template_name = 'horario.html'


def pensum(request):
    ma=Materia.objects.all()
    p=Pensum.objects.all()
    return render_to_response('pensum.html',locals(),context_instance=RequestContext(request))

def opcioncalificacion(request):
    return render_to_response('OpcionCalificaciones.html',context_instance=RequestContext(request))

def matricula(request):
    return render_to_response('matricula.html',context_instance=RequestContext(request))

def matriculamateria(request):
    m=Materia.objects.all()
    g=Grupo.objects.all()
    return render_to_response('matricula_materia.html',locals(),context_instance=RequestContext(request))

def horario(request):
    return render_to_response('horario.html',context_instance=RequestContext(request))

def financiera(request):
    return render_to_response('matriculafinanciera.html',context_instance=RequestContext(request))

def Hojavida(request,ced):
    e=Estudiante.objects.get(documento=ced)
    return render_to_response('hojadevida.html',locals(),context_instance=RequestContext(request))