from django.db import models
from django.contrib.auth.models import User

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
    lugar_nacimiento=models.ForeignKey(Ciudad,related_name="nacimiento")
    fecha_nacimiento=models.DateField()
    direccion=models.CharField(max_length=100)
    telefono=models.IntegerField()
    correo=models.EmailField(blank=True,null=True,unique=True)
    usuario = models.OneToOneField(User,null=True,blank=True)

    def __unicode__(self):
        return  self.primer_nombre + " "+self.primer_apellido+" "+self.segundo_apellido



class Facultad(models.Model):
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)

     def __unicode__(self):
        return self.nombre

     class Meta:
        #nombre en plural del modelo
        verbose_name_plural='Facultades'
        #nombre de la tabla por defecto es :nombreapp_nombremodelo
        db_table="Facultad"



class Programa(models.Model):
     facultad=models.ForeignKey(Facultad)
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)

     def __unicode__(self):
        return self.nombre

     class Meta:
         db_table="Programa"

class JefeDepartamento(Persona):
     programa=models.OneToOneField(Programa)

class Bloque(models.Model):
     nombre=models.CharField(max_length=2,primary_key=True)

     def __unicode__(self):
        return self.nombre

class Aula(models.Model):
     bloque=models.ForeignKey(Bloque)
     nombre=models.CharField(max_length=50)

     def __unicode__(self):
        return self.nombre + "-" + self.bloque.nombre

     class Meta:
         #llave compuesta en django
         unique_together=('bloque','nombre')

class Materia(models.Model):
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)
     creditos=models.IntegerField()
     prerequisito=models.ForeignKey('self',related_name="materia",null=True,blank=True)

     def __unicode__(self):
        return  self.nombre

     class Meta:
         db_table="Materia"

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

    def __unicode__(self):

        return self.dia +"  " +   self.horainicio.strftime('%H:%M')+'-'+self.horafinal.strftime('%H:%M')

class HorarioAula(models.Model):
    hora=models.ForeignKey(Hora)
    aula=models.ForeignKey(Aula)

    def __unicode__(self):

        return self.aula.nombre+self.aula.bloque.nombre +' - '+ str(self.hora)

    class Meta:
        unique_together=('hora','aula')


class Pensum(models.Model):
     codigo=models.CharField(primary_key=True,max_length=10)
     nombre=models.CharField(max_length=50)
     creditos=models.IntegerField()
     programa=models.ForeignKey(Programa)
     materias=models.ManyToManyField(Materia)

     def __unicode__(self):
        return self.nombre

class PrecioMatricula(models.Model):
     codigo=models.CharField(primary_key=True,max_length=10)
     facultad=models.ForeignKey(Facultad)
     precio=models.FloatField()

     def __unicode__(self):
        return self.codigo +'-'+self.facultad.nombre

