from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from django.template import RequestContext

from Administrativo.models import *
from .models import Estudiante,MatriculaAcademica
from Docente.models import Grupo
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy

from django.views.generic import TemplateView,ListView,CreateView,DeleteView,UpdateView,DetailView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from Estudiante.forms import FormularioLogin,FormularioRegistro

class Index(FormView):
    template_name = "index.html"
    form_class = FormularioLogin

    def form_valid(self, form):
        usr = form.cleaned_data['usuario']
        psw = form.cleaned_data['contrasena']
        autenticacion = authenticate(username=usr, password=psw)
        if autenticacion is not None:
            print("Valido")
            if autenticacion.is_active:
                login(self.request,autenticacion)
                e=Estudiante.objects.get(documento=1065658040)
                return redirect(reverse_lazy('home',kwargs={'pk': e.documento }))
            else:
                 return redirect(reverse_lazy('index'))
        else:

            return render_to_response('signin.html',{"estado":"Error de Usuario o Contrasena","form":form},context_instance=RequestContext(self.request))
        return super(Login, self).form_valid(form)

class Logueado(DetailView):
    model = Estudiante
    template_name = "home.html"



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

def horario(request):
    return render_to_response('horario.html',context_instance=RequestContext(request))

def financiera(request):
    return render_to_response('matriculafinanciera.html',context_instance=RequestContext(request))

def Hojavida(request,ced):
    e=Estudiante.objects.get(documento=ced)
    return render_to_response('hojadevida.html',locals(),context_instance=RequestContext(request))

class CrearEstudiante(CreateView):
    model = Facultad
    template_name = 'createview.html'
    fields = ['codigo','nombre']
    success_url = "/lista"
    def form_valid(self, form):
        print("valido")
        return super(CrearEstudiante,self).form_valid(form)

    def form_invalid(self, form):
        print("invalido")
        return super(CrearEstudiante,self).form_invalid(form)

class ListaEstudiante(ListView):
    template_name = 'listview.html'
    model = Facultad

class DetalleEstudiante(DetailView):
    template_name = 'hojadevida.html'
    model = Estudiante

class ElimnarFacultad(DeleteView):
    template_name = 'deleteview.html'
    model=Facultad
    success_url = "/lista"

class ActulizarFacultad(UpdateView):
    template_name = 'updateview.html'
    model=Facultad
    fields = ['codigo','nombre']
    success_url = "/lista"

class RegistroEstudiante(CreateView):
    template_name = 'registroestudiante.html'
    model = Estudiante
    success_url = '/'
    form_class = FormularioRegistro

class ListaGrupos(ListView):
    template_name = 'matricula_materia.html'
    model = Grupo

    def get_context_data(self, **kwargs):
        context = super(ListaGrupos, self).get_context_data(**kwargs)
        m=Materia.objects.all()
        context['grupo']=Grupo.objects.filter(materia='m1')
        context['materias']=Materia.objects.all()
        return context

class HorarioMateria(DetailView):
    template_name = 'horariomateria.html'
    model = Grupo


class ListaMateriasGrupos(ListView):
    template_name = 'matricula.html'
    model = MatriculaAcademica