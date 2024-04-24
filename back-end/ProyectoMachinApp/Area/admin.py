from django.contrib import admin
from .models import Area

@admin.register(Area)
class areaAdmin(admin.ModelAdmin):
    list_display = ['area_fk_sedes', 'area_nombre']