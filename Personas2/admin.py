from django.contrib import admin
from .models import Persona

class PersonasAdmin(admin.ModelAdmin):
    list_display=('id','nombre', 'apellido','dni','sexo','fecha_nac', 'foto' ,'created')
    reactonly_field=('created','update')
    search_fields=('nombre','apellido','dni') #buscador
    list_filter=('sexo','estado_civil','created') #filtro
    date_hierarchy='fecha_nac' #filtro superior por año y mes

admin.site.register(Persona,PersonasAdmin)
# Register your models here.
