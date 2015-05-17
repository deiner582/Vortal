from django.db import models
from Administrativo.models import Persona

class Profesion(models.Model):
    codigo=models.CharField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural='Profesiones'

class Docente(Persona):
    profesion=models.ForeignKey(Profesion)