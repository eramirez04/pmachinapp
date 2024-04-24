from django.db import models

# Create your models here.

class Tipo_equipo(models.Model):
    idTipo_equipo= models.AutoField(primary_key=True)
    ti_fi_nombre = models.CharField(max_length=100)


def __str__(self):
    return self.ti_fi_nombre
