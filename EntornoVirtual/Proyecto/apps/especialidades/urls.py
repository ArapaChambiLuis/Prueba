from django.conf.urls import url

from apps.especialidades.views import principal,   \
   PersonaList, PersonaCreate



urlpatterns = [
    url(r'^Principal', principal,name='Principal'),
    url(r'^RegistrarPersona',PersonaCreate.as_view(),name ='RegistrarPersona'),
    url(r'^VerPersonas', PersonaList.as_view(),name='VerPersonas'),
    url(r'^DetallePersona', principal,name='DetallePersona'),

]