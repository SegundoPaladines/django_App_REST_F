from rest_framework import serializers
from .models import Facultad, Programa, Docente

class FacultadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Facultad
        fields = ('pk', 'universidad', 'name', 'logo', 'pub_date')
        
class ProgramaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programa
        fields = ('pk', 'facultad', 'name', 'logo', 'pub_date')
        
class DocenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Docente
        #si igual los voy a traer todos, es mejor asi
        fields = ('__all__')