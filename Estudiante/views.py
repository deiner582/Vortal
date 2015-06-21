from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from django.template import RequestContext

from Administrativo.models import *
from .models import Estudiante,MatriculaAcademica,MatriculaFinanciera
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
                e=Estudiante.objects.get(usuario=self.request.user)
                return redirect(reverse_lazy('home',kwargs={'pk': e.documento }))
            else:
                 return redirect(reverse_lazy('index'))
        else:

            return render_to_response('signin.html',{"estado":"Error de Usuario o Contrasena","form":form},context_instance=RequestContext(self.request))
        return super(Login, self).form_valid(form)

class Logueado(DetailView):
    model = Estudiante
    template_name = "home.html"



class HorarioView(DetailView):
    model = Estudiante
    template_name = 'horario.html'

    def get_context_data(self, **kwargs):
        context = super(HorarioView, self).get_context_data(**kwargs)
        context['m']=MatriculaAcademica.objects.filter(estudiante=self.object)
        return context

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

class MatriculaFinancier(DetailView):
    template_name = 'matriculafinanciera.html'
    model = Estudiante

    def get_context_data(self, **kwargs):
        context = super(MatriculaFinancier, self).get_context_data(**kwargs)
        context['m']=MatriculaFinanciera.objects.filter(estudiante=self.object)
        return context


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

class ListaGrupos(DetailView):
    template_name = 'matricula_materia.html'
    model = Estudiante
    context_object_name = "estudiante"

    def get_context_data(self, **kwargs):
        dict={}
        context = super(ListaGrupos, self).get_context_data(**kwargs)
        materias=Materia.objects.all()
        for m in materias:
            g=Grupo.objects.filter(materia=m)
            if len(g)==0:
                dict[m]="0"
            else:
                 dict[m]=g
        context['dic'] = dict
        return context
'''
def HorarioGrupo(request,gr,cod):
    e=Grupo.objects.filter(materia=cod,grupo=gr)
    return render_to_response('horariomateria.html',locals(),context_instance=RequestContext(request)'''

class HorarioGrupo(DetailView):
    template_name = 'horariomateria.html'
    model = Estudiante


    def get_context_data(self, **kwargs):
        context = super(HorarioGrupo, self).get_context_data(**kwargs)
        context['m']=MatriculaAcademica.objects.filter(estudiante=self.object)
        #self.kwargs accede a los parametros de una url
        context['e']=Grupo.objects.filter(materia=self.kwargs['cod'],grupo=self.kwargs['gr'])
        return context

class ListaMateriasGrupos(DetailView):
    template_name = 'matricula.html'
    model = Estudiante

    def get_context_data(self, **kwargs):
        context = super(ListaMateriasGrupos, self).get_context_data(**kwargs)
        context['m']=MatriculaAcademica.objects.filter(estudiante=self.object)
        return context

class Angular(TemplateView):
    template_name = 'angular.html'
