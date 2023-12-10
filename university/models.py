from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse
import os

# Modelo para la facultad
class Facultad(models.Model):
    """ Una facultad """
    universidad = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='media/facultades/logos/')
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('lista-facultades')

# Borrar la imagen del logo cuando es eliminada la facultad
@receiver(post_delete, sender=Facultad)
def delete_fac_logo(sender, instance, **kwargs):
    if instance.logo:
        if os.path.isfile(instance.logo.path):
            os.remove(instance.logo.path)
            
##-----------------------------------------------------------------------------------------------##

# Modelo para el programa
class Programa(models.Model):
    """ Un Programa"""
    facultad = models.ForeignKey('Facultad', on_delete=models.CASCADE, related_name='get_programas' )
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='media/programas/logos/')
    pub_date = models.DateField(auto_now_add=True)
    
    def get_absolute_url(self):
            return reverse('lista-programas')
        
    def __str__(self):
        return self.name
    
# Borrar la imagen del logo cuando el programa es eliminado
@receiver(post_delete, sender=Programa)
def delete_prog_logo(sender, instance, **kwargs):
    if instance.logo:
        if os.path.isfile(instance.logo.path):
            os.remove(instance.logo.path)

##------------------------------------------------------------------------------------------------------------##

# Modelo para los docentes
class Docente(models.Model):
    """ Docentes """
    programa = models.ForeignKey('Programa', on_delete=models.CASCADE,related_name='get_docentes' )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    formacion = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/docentes/fotos/')
    pub_date = models.DateField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('lista-docentes')
    
    def __str__(self):
        return self.first_name + " " + self.last_name

# Borrar la foto del docente cuando es eliminado
@receiver(post_delete, sender=Docente)
def delete_doc_photo(sender, instance, **kwargs):
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)