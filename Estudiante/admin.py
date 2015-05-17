from django.contrib import admin
from .models import Estudiante



class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("documento","primer_nombre","primer_apellido","programa")


admin.site.register(Estudiante,EstudianteAdmin)