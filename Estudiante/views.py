from django.shortcuts import render,redirect,render_to_response,get_object_or_404
from django.template import RequestContext

from Administrativo.models import *
from .models import Estudiante,MatriculaAcademica,MatriculaFinanciera,Nota
from Docente.models import Grupo
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView,ListView,CreateView,DeleteView,UpdateView,DetailView, View
from django.contrib.auth import authenticate, login, logout
from Estudiante.forms import FormularioLogin,FormularioRegistro,FormularioMatriculaAcademica

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

class pensum(DetailView):
    model = Estudiante
    template_name = 'pensum.html'

    def get_context_data(self, **kwargs):
        context = super(pensum, self).get_context_data(**kwargs)
        print(self.kwargs['pr'])
        context['p']=Pensum.objects.filter(programa=self.kwargs['pr'])
        print(context['p'])
        return context



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


    def get_context_data(self, **kwargs):
        dict={}
        mat=[]
        context = super(ListaGrupos, self).get_context_data(**kwargs)
        materias=Materia.objects.all()
        matricula=MatriculaAcademica.objects.filter(estudiante=self.kwargs['pk'])
        #matricula
        for ma in matricula:
            mat=ma.grupos.materia.nombre
        #materias
        for m in materias:
            g=Grupo.objects.filter(materia=m)
            for ma in g:
                materias= str(ma.materia)
                #si la materia no esta en la matricula academica del estudiante la agrago al diccionario
                if materias not in mat:
                    dict[m]=g
        context['dic'] = dict
        return context


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

class MatricularMateria(DetailView):
    template_name = 'matricula_exitosa.html'
    model = Estudiante

    def get_context_data(self, **kwargs):
        context = super(MatricularMateria, self).get_context_data(**kwargs)
        e=Estudiante.objects.get(documento=self.kwargs['pk'])
        gr=Grupo.objects.get(grupo= int(self.kwargs['gr']),materia=Materia.objects.get(codigo=self.kwargs['cod']))
        matr=MatriculaAcademica(estudiante=e,grupos=gr)
        context["grupo"]=Grupo.objects.get(grupo= int(self.kwargs['gr']),materia=Materia.objects.get(codigo=self.kwargs['cod']))
        matr.save()
        return context

class EliminarMateria(DetailView):
    template_name = 'eliminarmateria.html'
    model = Estudiante

    def get_context_data(self, **kwargs):
        context = super(EliminarMateria, self).get_context_data(**kwargs)
        e=Estudiante.objects.get(documento=self.kwargs['pk'])
        gr=Grupo.objects.get(grupo= int(self.kwargs['gr']),materia=Materia.objects.get(codigo=self.kwargs['cod']))
        matr=MatriculaAcademica.objects.filter(estudiante=e,grupos=gr)
        matr.delete()
        context["grupo"]=Grupo.objects.get(grupo= int(self.kwargs['gr']),materia=Materia.objects.get(codigo=self.kwargs['cod']))
        return context

class Opcion(DetailView):
    template_name = 'OpcionCalificaciones.html'
    model = Estudiante

class Notas(DetailView):
    template_name = 'notas.html'
    model = Estudiante

    def get_context_data(self, **kwargs):
        n=[]
        notaf=0.0
        context = super(Notas, self).get_context_data(**kwargs)
        estudiante=Estudiante.objects.get(documento=self.kwargs['pk'])
        matricula=MatriculaAcademica.objects.filter(estudiante=estudiante)
        for m in matricula:
            nota=Nota.objects.filter(matriculaacedemica=m)
            n.append(nota)
        context["notas"]=n
        for no in n:
            print(no)
        context["promedio"]=notaf
        return context