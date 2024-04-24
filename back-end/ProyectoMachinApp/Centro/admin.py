from django.contrib import admin
from .models import Centro

@admin.register(Centro)
class centroAdmin(admin.ModelAdmin):
    list_display = ['cen_nombre', 'cen_descripcion', 'cen_regional', 'cen_municipio', 'cen_subdirector']