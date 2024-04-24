from django.db import models
from django.db.models import SET_NULL
from Sede.models import Sede

class Area(models.Model):
    area_fk_sedes = models.ForeignKey(Sede, on_delete=SET_NULL, null=True)
    area_nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.area_nombre