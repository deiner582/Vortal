from django.contrib import admin
from .models import Estudiante,Etnia,MatriculaAcademica



class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("documento","primer_nombre","primer_apellido","programa",'estado')
class EtniaAdmin(admin.ModelAdmin):
    list_display = ("codigo","nombre")

admin.site.register(Estudiante,EstudianteAdmin)
admin.site.register(Etnia,EtniaAdmin)
admin.site.register(MatriculaAcademica)