from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

#modelo para la facultad
class Facultad(models.Model):
    """ Una facultad """
    universidad = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='facultades/logos/')
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('lista-facultades')
    
#modelo para el programa
class Programa(models.Model):
    """ Un Programa"""
    facultad = models.ForeignKey('Facultad', on_delete=models.CASCADE, related_name='get_programas' )
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='programas/logos/')
    pub_date = models.DateField(auto_now_add=True)
    
    def get_absolute_url(self):
            return reverse('lista-programas')
        
    def __str__(self):
        return self.name

#modelo docentes
class Docente(models.Model):
    """ Docentes """
    programa = models.ForeignKey('Programa', on_delete=models.CASCADE,related_name='get_docentes' )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    formacion = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='docentes/fotos/')
    pub_date = models.DateField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('lista-docentes')
    
    def __str__(self):
        return self.first_name + " " + self.last_name
