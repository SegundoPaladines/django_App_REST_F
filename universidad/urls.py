"""
URL configuration for universidad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from university import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('universidad/facultades/', views.FacultadesListView.as_view(), name='lista-facultades'), #todas las facultades
    path('facultad/<int:pk>/detail/',
         views.FacultadDetailView.as_view(), name='fac-detail'),
    path('universidad/programas/', views.ProgramasListView.as_view(), name='lista-programas'), #todos los programas
    path('programa/<int:pk>/detail/',
            views.ProgramaDetailView.as_view(), name='prog-detail'),
    path('universidad/docentes/', views.DocentesListView.as_view(), name='lista-docentes'), #todos los docentes
    path('docente/<int:pk>/detail/',
            views.DocenteDetailView.as_view(), name='doc-detail'),
]