from django.contrib import admin
from .models import Profesion,Docente

class ProfesionAdmin(admin.ModelAdmin):
    list_display = ("codigo","nombre")
    list_filter = ("codigo","nombre")

class DocenteAdmin(admin.ModelAdmin):
    list_display = ("documento","primer_nombre","primer_apellido","profesion")

admin.site.register(Docente,DocenteAdmin)
admin.site.register(Profesion,ProfesionAdmin)