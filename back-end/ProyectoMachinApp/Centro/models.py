from django.db import models

class Centro(models.Model):
    cen_nombre = models.CharField(max_length=200)
    cen_descripcion = models.CharField(max_length=255)
    cen_regional = models.CharField(max_length=100)
    cen_municipio = models.CharField(max_length=100)
    cen_subdirector = models.CharField(max_length=100)
        
    def __str__(self):
        return self.cen_nombre