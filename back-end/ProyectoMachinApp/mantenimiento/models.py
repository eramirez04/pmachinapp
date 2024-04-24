from django.db import models
from django.db.models import SET_NULL
from tipo_mantenimiento.models import tipo_mantenimiento_models

class mantenimiento_models(models.Model):
    mant_codigo_mantenimiento = models.CharField(max_length=50)
    mant_fecha_realizacion = models.DateTimeField(auto_created=True)
    mant_fecha_proxima = models.DateTimeField(auto_created=True)
    """ mant_fk_fichas = models.IntegerField(default=0) """
    mant_fk_mantenimiento = models.ForeignKey(tipo_mantenimiento_models, on_delete = SET_NULL, null=True)
    mant_descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.mant_codigo_mantenimiento