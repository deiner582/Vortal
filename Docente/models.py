from django.db import models
from Administrativo.models import Persona,Materia,HorarioAula

class Profesion(models.Model):
    codigo=models.CharField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural='Profesiones'

class Docente(Persona):
    profesion=models.ForeignKey(Profesion)

class Grupo(models.Model):
    grupo=models.IntegerField()
    materia=models.ForeignKey(Materia)
    profesor=models.ForeignKey(Docente)
    horario=models.ManyToManyField(HorarioAula)


    def __unicode__(self):
        #conversion a string de grupo ya que es un entero y solo se puede retornar string
        return  str(self.grupo)

    class Meta:
        unique_together=('grupo','materia')
        db_table="Grupo"