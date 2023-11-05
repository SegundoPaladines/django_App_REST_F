from django.urls import reverse_lazy 
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView, ListView, DetailView
from university.models import Facultad, Programa, Docente

# Create your views here.
class UniversidadView(TemplateView):
    template_name='universidad.html'

class FacultadesListView(ListView):
    model = Facultad
    template_name = "fac_list.html"
    
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
    
class ProgramasListView(ListView):
    model = Programa
    template_name = "prog_list.html"

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
