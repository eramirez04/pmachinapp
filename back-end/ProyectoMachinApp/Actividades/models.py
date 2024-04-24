from django.db import models

# Create your models here.

class Actividades (models.Model):
    idActividades = models.IntegerField()
    acti_nombre = models.CharField(max_length=255)
    acti_descripcion = models.TextField()
    acti_fecha_realizacion = models.DateTimeField(auto_now_add=True)
    acti_estado = models.CharField(max_length=255)
    fk_mantenimiento = models.IntegerField()
    
    def __str__(self) -> str:
        return self.acti_nombre