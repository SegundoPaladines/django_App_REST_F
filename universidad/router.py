##REST FRAMEWORK
from university import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'fac_rest', views.FacultadViewSet)
router.register(r'prog_rest', views.ProgramaViewSet)
router.register(r'doc_rest', views.DocenteViewSet)