from django.contrib import admin
from .models import TipoSitio

@admin.register(TipoSitio)
class TipoSitioAdmin(admin.ModelAdmin):
    list_display = ['tipo_sitio']