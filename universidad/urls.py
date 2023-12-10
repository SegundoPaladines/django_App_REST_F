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
from django.contrib.auth.decorators import login_required #para que toque authenticarse

##------------------------------------------------------------------------------------------------------##
##Dar visibilidad a los archivos de media:
from django.conf import settings
from django.conf.urls.static import static

##--------------------------------------------------------------------------------------------------------##
##REST FRAMEWORK
from django.urls import include
from .router import router

##---------------------------------------------------------------------------------------------------------##

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #no requieren autenticacion
    #bienvenida
    path('', views.UniversidadView.as_view(), name='udenar'), 
    
    #Facultades
    path('universidad/facultades/', views.FacultadesListView.as_view(), name='lista-facultades'), #detalle de la facultad
    path('facultad/<int:pk>/detail/',
         views.FacultadDetailView.as_view(), name='fac-detail'),
    
    # Programas
    path('universidad/programas/', views.ProgramasListView.as_view(), name='lista-programas'), #Todos los programas
    path('programa/<int:pk>/detail/',
            views.ProgramaDetailView.as_view(), name='prog-detail'),
    
    # docentes
    path('universidad/docentes/', views.DocentesListView.as_view(), name='lista-docentes'), #todos los docentes
    path('docente/<int:pk>/detail/',
            views.DocenteDetailView.as_view(), name='doc-detail'),

    #las que requieren autenticacion
    path('facultad/<int:pk>/update/', login_required(views.FacultadUpdate.as_view()), name='fac-update'),  # Editar facultad
    path('facultad/<int:pk>/delete/', login_required(views.FacultadDelete.as_view()), name='fac-delete'),  # Eliminar facultad
    path('facultad/create/', login_required(views.FacultadCreate.as_view()), name='fac-create'),  # Crear facultad

    path('programa/<int:pk>/update/', login_required(views.ProgramaUpdate.as_view()), name='prog-update'),  # Editar programa
    path('programa/<int:pk>/delete/', login_required(views.ProgramaDelete.as_view()), name='prog-delete'),  # Eliminar programa
    path('programa/create/', login_required(views.ProgramaCreate.as_view()), name='prog-create'),  # Crear programa

    path('docente/<int:pk>/update/', login_required(views.DocenteUpdate.as_view()), name='doc-update'),  # Editar docente
    path('docente/<int:pk>/delete/', login_required(views.DocenteDelete.as_view()), name='doc-delete'),  # Eliminar docente
    path('docente/create/', login_required(views.DocenteCreate.as_view()), name='doc-create'),  # Crear docente

    ##----------------------------------------------------------------------------------------------------------------------------------------##
    ##REST FRAMEWORK
    path('res/', include(router.urls)),
    path('api/',include('rest_framework.urls', namespace='rest_framework')),
]

##---------------------------------------------------------------------------------------------------------##
##Dar visibilidad a los archivos de media:

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)