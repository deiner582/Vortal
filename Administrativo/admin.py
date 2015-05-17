from django.contrib import admin
from .models import *

# Register your models here.
class MateriasAdmin(admin.ModelAdmin):
    list_display = ("codigo","nombre","creditos","prerequisito")

class ProgramaAdmin(admin.ModelAdmin):
    list_display = ("codigo","nombre","facultad")
    fieldsets = [

        ('Programa', {
            'fields': ['codigo', 'nombre'],
        }),
        ('Facultad', {
            'fields': [ 'facultad'],

        }),
    ]
class FacultadAdmin(admin.ModelAdmin):
    list_display = ("codigo","nombre")

class AulaAdmin(admin.ModelAdmin):
    list_display = ("nombre","bloque")

class CiudadAdmin(admin.ModelAdmin):
    list_display = ("codigo","nombre","departamento")

class GrupoAdmin(admin.ModelAdmin):
    list_display = ("codigo","grupo","materia")

class HoraAdmin(admin.ModelAdmin):
    list_display = ("codigo","dia","horainicio","horafinal","aula")

admin.site.register(Programa,ProgramaAdmin)
admin.site.register(Materia,MateriasAdmin)
admin.site.register(Facultad,FacultadAdmin)
admin.site.register(Bloque,FacultadAdmin)
admin.site.register(Aula,AulaAdmin)
admin.site.register(Pensum)
admin.site.register(Hora,HoraAdmin)
admin.site.register(Grupo,GrupoAdmin)
admin.site.register(Ciudad,CiudadAdmin)
admin.site.register(Departamento,FacultadAdmin)