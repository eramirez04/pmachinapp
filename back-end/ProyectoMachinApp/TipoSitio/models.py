from django.db import models

class TipoSitio(models.Model):
    tipo_sitio = models.CharField(max_length=255)
    
    def __str__(self):
        return self.sit_nombre