from django.contrib import admin
from .models import Sitio

@admin.register(Sitio)
class sitioAdmin(admin.ModelAdmin):
    list_display = ['sit_fk_areas', 'sit_fk_tipo_sitio', 'sit_nombre']