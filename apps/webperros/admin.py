from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.
class resourcelibro(resources.ModelResource):
    class Meta:
        model = libro

class Adminlibro(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['autor','paginas','fecha_de_lanzamiento','idioma','disponibilidad','precio']
    resource_class = resourcelibro
admin.site.register(libro, Adminlibro)


class resourcecategorias(resources.ModelResource):
    class Meta:
        model = categorias

class Admincategorias(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['variedad']
    list_display = ['editorial','fk_libro']
    resource_class = resourcecategorias

admin.site.register(categorias, Admincategorias)


