from django.shortcuts import render
from apps.especialidades.forms import formP
from django.views.generic import ListView,CreateView
from django.core.urlresolvers import reverse_lazy
from django import templatetags

from apps.especialidades.models import Persona

# Create your views here.
def principal(request):
    return render(request, "App/Principal.html")

class PersonaCreate(CreateView):
    model = Persona
    form_class = formP
    template_name = 'App/persona_form.html'
    success_url = reverse_lazy('VerPersonas')

class PersonaList(ListView):
    model = Persona
    template_name = 'App/Personas_listar.html'

