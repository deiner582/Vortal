from django.db import models
from Administrativo.models import Persona,Programa


class Estudiante(Persona):
    programa=models.ForeignKey(Programa)
