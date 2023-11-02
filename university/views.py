from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from university.models import Facultad, Programa, Docente

# Create your views here.

class FacultadesListView(ListView):
    model = Facultad
    template_name = "fac_list.html"
    
class FacultadDetailView(DetailView):
    model = Facultad
    template_name = "fac_detail.html"

class ProgramasListView(ListView):
    model = Programa
    template_name = "prog_list.html"

class ProgramaDetailView(DetailView):
    model = Programa
    template_name = "prog_detail.html"

class DocentesListView(ListView):
    model = Docente
    template_name = "doc_list.html"

class DocenteDetailView(DetailView):
    model = Docente
    template_name = "doc_detail.html"
