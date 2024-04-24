from django.db import models
from django.db.models import SET_NULL
from Area.models import Area
from TipoSitio.models import TipoSitio

class Sitio(models.Model):
    sit_nombre = models.CharField(max_length=100)
    sit_fk_areas = models.ForeignKey(Area, on_delete=SET_NULL, null=True)
    sit_fk_tipo_sitio = models.ForeignKey(TipoSitio, on_delete=SET_NULL, null=True)
    
    def __str__(self):
        return self.sit_nombre