from django.db import models
from django.db.models import SET_NULL
from Centro.models import Centro

class Sede(models.Model):
    sede_fk_centros = models.ForeignKey(Centro, on_delete=SET_NULL, null=True)
    sede_nombre = models.CharField(max_length=255)
    sede_descripcion = models.TextField()
    sede_direccion = models.CharField(max_length=250)
    
    def __str__(self):
        return self.sede_nombre