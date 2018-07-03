from django.conf.urls import url

from apps.especialidades.views import *



urlpatterns = [
    url(r'^Principal', principal,name='Principal'),

    url(r'^RegistrarPersona',PersonaCreate.as_view(),name ='RegistrarPersona'),
    url(r'^RegistrarProfesion',ProfesionCreate.as_view(),name ='RegistrarProfesion'),
    url(r'^RegistrarExperiencia',ExperienciaCreate.as_view(),name ='RegistrarExperiencia'),
    url(r'^RegistrarCapacitacion',CapacitacionCreate.as_view(),name ='RegistrarCapacitacion'),

    url(r'^MayorDetalle/(?P<Persona_id>\d+)/$',especialidades,name ='VerDatosGener'),
    url(r'^VerProfesion/(?P<Persona_id>\d+)/$',profesiones,name ='VerProfesion'),
    url(r'^VerExperiencia/(?P<Persona_id>\d+)/$',experiencias,name ='VerExperiencia'),
    url(r'^VerCapacitacion/(?P<Persona_id>\d+)/$',capacitaciones,name ='VerCapacitacion'),

    url(r'^VerPersonas', PersonaList.as_view(),name='VerPersonas'),
    url(r'^VerDetalle/(?P<pk>\d+)/$', dat_gen,name='DetallePersona'),
    url(r'^Buscar/(?P<name>\d+)/$', buscar,name='BuscarPersona'),

]