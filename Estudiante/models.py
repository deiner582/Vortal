from django.db import models
from Administrativo.models import Persona,Programa,PrecioMatricula
from Docente.models import Grupo
class Etnia(models.Model):
    codigo=models.CharField(primary_key=True,max_length=10)
    nombre=models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

class Estudiante(Persona):
    Estrato= (
   ('1', '1'),
   ('2', '2'),
   ('3', '3'),
   ('4', '4'),
   ('5', '5'),
   ('6', '6'),
    )
    Estado= (
   ('Admitido', 'Admitido'),
   ('Inscripto', 'Inscripto'),
   ('Activo', 'Activo'),
   ('Inactivo', 'Inactivo'),
   ('PFU', 'PFU'),
    )
    etnia=models.ForeignKey(Etnia,default="Ninguna")
    programa=models.ForeignKey(Programa)
    estrato=models.CharField(max_length=1,choices=Estrato,default=1)
    estado=models.CharField(max_length=9,choices=Estado,default="Inscripto",null=True,blank=True)

class MatriculaAcademica(models.Model):
    codigo=models.CharField(primary_key=True,max_length=20)
    estudiante=models.ForeignKey(Estudiante)
    grupos=models.ManyToManyField(Grupo)

    def __unicode__(self):
        return self.codigo+"-"+self.estudiante.primer_nombre+" "+self.estudiante.primer_apellido

class MatriculaFinanciera(models.Model):
    Periodo= (
   ('1', '1'),
   ('2', '2'),
    )
    Estado= (
   ('Pagado', 'Pagado'),
   ('Pendiente', 'Pendiente'),
    )
    referencia=models.CharField(primary_key=True,max_length=20)
    estudiante=models.ForeignKey(Estudiante)
    precio=models.ForeignKey(PrecioMatricula)
    descuento=models.FloatField()
    ano=models.DateField()
    periodo=models.CharField(max_length=2,choices=Periodo)
    estado=models.CharField(max_length=10,choices=Estado,default="Pendiente",null=True,blank=True)

    def __unicode__(self):
        return self.referencia+"-"+str(self.estudiante.documento)+"- "+self.estudiante.primer_apellido