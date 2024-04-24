from django.contrib import admin
from .models import Sede

@admin.register(Sede)
class sedeAdmin(admin.ModelAdmin):
    list_display = ['sede_fk_centros', 'sede_nombre', 'sede_descripcion', 'sede_direccion']