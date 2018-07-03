from django.shortcuts import render_to_response,render
from apps.especialidades.forms import *
from django.views.generic import ListView,CreateView,TemplateView,RedirectView,UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.especialidades.models import Persona,PerProfesion,Experiencia,Capacitacion

# Create your views here.
def principal(request):
    return render(request, "App/Principal.html")

class PersonaCreate(CreateView):
    model = Persona
    form_class = formP
    template_name = 'App/persona_form.html'
    success_url = reverse_lazy('RegistrarProfesion')

class ProfesionCreate(CreateView):
    model = PerProfesion
    form_class = form_PerProfesion
    template_name = 'App/reg_per_profesion.html'
    success_url = reverse_lazy('RegistrarExperiencia')

class ProfesionUpDate(UpdateView):
    model = PerProfesion
    form_class = form_act_profesion
    template_name = 'App/actualizar_profesion.html'
    success_url = reverse_lazy('VerDatosGener')

class ExperienciaCreate(CreateView):
    model = Experiencia
    form_class = form_Experiencia
    template_name = 'App/reg_experiencia.html'
    success_url = reverse_lazy('RegistrarCapacitacion')

class CapacitacionCreate(CreateView):
    model =Capacitacion
    form_class = form_Capacitacion
    template_name = 'App/reg_capacitacion.html'
    success_url = reverse_lazy('VerPersonas')

class PersonaList(ListView):
    model = Persona
    template_name = 'App/Personas_listar.html'

class PersonaVerDetalle(UpdateView):
    context_object_name = 'object_datos'
    model = Persona
    form_class = formP
    template_name = 'App/Personas_ver.html'

class PersonaVerProf(ListView):
   model = PerProfesion
   template_name = 'App/ver_profesion.html'

def dat_gen(request,pk):
    lista_todos = Persona.objects.get(id=pk)
    return render_to_response('App/Personas_ver.html',{ 'per' : lista_todos})

class profesiones_list(ListView):
   model = PerProfesion
   template_name = 'App/ver_profesion.html'

def prof(Persona_id):
    i = 2
    lista = []
    while (i > 1):
        obj = PerProfesion.objects.get(CodPers=Persona_id)
        if (obj == ()):
            i = 1
        else:
            lista.append(obj)
    return lista
def datos_generales (request,Persona_id):
    lista = PerProfesion.objects.filter(CodPers=Persona_id)
    return render_to_response('App/Personas_ver.html',{ 'per' : lista })

def profesiones(request,Persona_id):
    lista = PerProfesion.objects.filter(CodPers=Persona_id)
    return render_to_response('App/ver_profesion.html',{ 'profesiones' : lista })

def experiencias(request,Persona_id):
    lista = Experiencia.objects.filter(CodPers=Persona_id)
    return render_to_response('App/ver_experiencia.html',{ 'experiencias' : lista})

def capacitaciones(request,Persona_id):
    lista = Capacitacion.objects.filter(CodPers=Persona_id)
    return render_to_response('App/ver_capacitacion.html',{ 'capacitaciones' : lista})

def especialidades(request,Persona_id):
    listd = Persona.objects.get(id=Persona_id)
    listp = PerProfesion.objects.filter(CodPers=Persona_id)
    liste = Experiencia.objects.filter(CodPers=Persona_id)
    listc = Capacitacion.objects.filter(CodPers=Persona_id)
    espe = [listd,listp,liste,listc]
    return render_to_response('App/Personas_ver.html', {'datos': listd, 'profesion': listp, 'capacitacion':listc, 'experiencia':liste })

def buscar(request,name):
    listd = Persona.objects.filter(name__contains=name)
    return render_to_response('App/Personas_buscar.html',{'object_list': listd })

