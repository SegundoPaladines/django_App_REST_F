from typing import Any
from django.urls import reverse_lazy 
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView, ListView, DetailView
from university.models import Facultad, Programa, Docente
import requests

##--------------------------------------------------------------------------------------------------------##

##imports para trabajar con django rest framework
from rest_framework import viewsets
from .serializers import FacultadSerializer, ProgramaSerializer, DocenteSerializer

##-------------------------------------------------------------------------------------------------------##

# Create your views here.
class UniversidadView(TemplateView):
    template_name='universidad.html'

##------------------------------------------------------------------------------------------------------##

##se consume desde la appi rest
class FacultadesListView(ListView):
    model = Facultad
    template_name = "fac_list.html"
    
    ##para consumir la appi
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Hacer la solicitud a la api
        ##link de la api
        api_url = "http://127.0.0.1:8000/fac_rest/"
        ## es una solicitud de tipo get <- para obtener cositas nada mas
        response = requests.get(api_url)
        
        # si el codigo de respuesta 200 significa que se obtuvo una respuesta correctamente
        if response.status_code == 200:
            #convertir el contenido JSON de la respuesta
            facultades = response.json()
            ##se guarda facultades en el contex que se va para ls vista
            context['facultades'] = facultades
            
        #devolvemos el context
        return context
    
class ProgramasListView(ListView):
    model = Programa
    template_name = "prog_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #Hcaer la solicitud
        ##link de la api
        api_url = "http://127.0.0.1:8000/prog_rest/"
        ## es una solicitud de tipo get <- para obtener cositas nada mas
        res = requests.get(api_url)
        
        #si responden correctamente
        if res.status_code == 200:
            ## que caiga el JSON
            programas = res.json()
            
            ##
            for programa in programas:
                partes_url = programa['facultad'].split('/')
                id_fac = partes_url[-2]
                
                programa['facultad_id'] = id_fac
                
            ##nueva solicitud para averiguar el nombre de la facultad
            api_url = "http://127.0.0.1:8000/fac_rest/"
            res = requests.get(api_url)
            
            #si la nueva solicitud se hace correctamente
            if res.status_code == 200:
                ## el JSON
                facultades = res.json()
                
                for programa in programas:
                    for facultad in facultades:
                        if facultad['pk'] == int(programa['facultad_id']):
                            programa['facultad_name'] = facultad['name']
            
            ##guardamos los programas en el context
            context['programas'] = programas
        
        #devolvemos el context
        return context
    
##--------------------------------------------------------------------------------------------------##
##No se consumen desde la appi

class FacultadDetailView(DetailView):
    model = Facultad
    template_name = "fac_detail.html"

class FacultadUpdate(UpdateView):
    model = Facultad
    fields = '__all__'
    template_name = "facultad_form.html"
    
class FacultadDelete(DeleteView):
    model = Facultad
    template_name = "facultad_confirm_delete.html"
    success_url = reverse_lazy('lista-facultades')

class FacultadCreate(CreateView):
    model = Facultad
    fields = '__all__'
    template_name = "facultad_form.html"

class ProgramaDetailView(DetailView):
    model = Programa
    template_name = "prog_detail.html"
    
class ProgramaUpdate(UpdateView):
    model = Programa
    fields = '__all__'
    template_name = "programa_form.html"
    
class ProgramaDelete(DeleteView):
    model = Programa
    template_name = "programa_confirm_delete.html"
    success_url = reverse_lazy('lista-programas')

class ProgramaCreate(CreateView):
    model = Programa
    fields = '__all__'
    template_name = "programa_form.html"

class DocentesListView(ListView):
    model = Docente
    template_name = "doc_list.html"

class DocenteDetailView(DetailView):
    model = Docente
    template_name = "doc_detail.html"
    
class DocenteUpdate(UpdateView):
    model = Docente
    fields = '__all__'
    template_name = "docente_form.html"
    
class DocenteDelete(DeleteView):
    model = Docente
    template_name = "docente_confirm_delete.html"
    success_url = reverse_lazy('lista-docentes')

class DocenteCreate(CreateView):
    model = Docente
    fields = '__all__'
    template_name = "docente_form.html"
    
##-----------------------------------------------------------------------------------------------##

##vistas del rest_framework
class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all().order_by('-pub_date')
    serializer_class = FacultadSerializer
    
class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all().order_by('-pub_date')
    serializer_class = ProgramaSerializer
    
class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all().order_by('-pub_date')
    serializer_class = DocenteSerializer
    
