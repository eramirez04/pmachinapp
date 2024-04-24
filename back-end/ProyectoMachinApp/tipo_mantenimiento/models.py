from django.db import models

class tipo_mantenimiento_models(models.Model):
    tipo_mantenimiento = models.CharField(max_length=50)
    

    def __str__(self):
        return self.tipo_mantenimiento
