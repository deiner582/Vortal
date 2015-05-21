from django.db import models
from django.contrib.auth.models import User
#from Docente.models import Profesion
# Create your models here.
class Departamento(models.Model):
    codigo=models.CharField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=50)


    def __unicode__(self):
        return self.nombre

class Ciudad(models.Model):
    codigo=models.CharField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=50)
    departamento=models.ForeignKey(Departamento)

    def __unicode__(self):
        return self.nombre+','+self.departamento.nombre

    class Meta:
        verbose_name_plural='Ciudades'

class Persona(models.Model):
    Sexo = (
   ('M', 'M'),
   ('F', 'F'),
    )
    Tipo=(('C.C','Cedula de ciudadania'),
          ('T.I','Tarjeta de identidad'),
          ('C.E','Cedula Extranjera'),
          ('Registro Civil','Registro Civil')
    )
    tipo_documento=models.CharField(choices=Tipo,max_length=20)
    documento=models.IntegerField(primary_key=True)
    lugar_expedicion=models.ForeignKey(Ciudad,related_name="expedicion")
    fecha_expedicion=models.DateField()
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre=models.CharField(max_length=30,null=True,blank=True)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido=models.CharField(max_length=30,null=True,blank=True)
    sexo=models.CharField(max_length=1,default='F',choices=Sexo)
    #nacimiento
    lugar_nacimiento=models.ForeignKey(Ciudad,related_name="nacimiento")
    fecha_nacimiento=models.DateField()
    #direccion
    direccion=models.CharField(max_length=100)
    telefono=models.IntegerField()
    correo=models.EmailField(blank=True,null=True,unique=True)
    usuario = models.OneToOneField(User,null=True,blank=True)

    def __unicode__(self):
        return  self.primer_nombre

class Facultad(models.Model):
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)

     def __unicode__(self):
        return self.nombre

     class Meta:
        #nombre en plural del modelo
        verbose_name_plural='Facultades'



class Programa(models.Model):
     facultad=models.ForeignKey(Facultad)
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)

     def __unicode__(self):
        return self.nombre

class JefeDepartamento(Persona):
     programa=models.OneToOneField(Programa)

class Bloque(models.Model):
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)

     def __unicode__(self):
        return self.nombre

class Aula(models.Model):
     bloque=models.ForeignKey(Bloque)
     nombre=models.CharField(primary_key=True,max_length=50)

     def __unicode__(self):
        return self.nombre + "-" + self.bloque.nombre

class Materia(models.Model):
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)
     creditos=models.IntegerField()
     prerequisito=models.ForeignKey('self',related_name="materia",null=True,blank=True)

     def __unicode__(self):
        return  self.nombre

class Hora(models.Model):
    Dias = (
   ('Lunes', 'Lunes'),
   ('Martes', 'Martes'),
   ('Miercoles', 'Miercoles'),
   ('Jueves', 'Jueves'),
   ('Viernes', 'viernes'),
   ('Sabado', 'Sabado'),
    )
    codigo=models.CharField(primary_key=True,max_length=10)
    dia=models.CharField(choices=Dias,max_length=20)
    horainicio=models.TimeField()
    horafinal=models.TimeField()
    aula=models.ForeignKey(Aula)

    def __unicode__(self):

        return self.dia


class Grupo(models.Model):
    codigo=models.CharField(primary_key=True,max_length=10)
    grupo=models.PositiveIntegerField()
    materia=models.ForeignKey(Materia)
    #profesor=models.ForeignKey(Docente)
    horas=models.ManyToManyField(Hora)
    #

    def __unicode__(self):
        return self.codigo

class Pensum(models.Model):
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)
     creditos=models.IntegerField()
     programa=models.ForeignKey(Programa)
     materias=models.ManyToManyField(Materia)

     def __unicode__(self):
        return self.nombre