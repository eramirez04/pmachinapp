from django.db import models

from tipoEquipo.models import Tipo_equipo

from django.db.models import SET_NULL

# Create your models here.

class Variable(models.Model):
    idVariable= models.AutoField(primary_key=True)
    var_nombre = models.CharField(max_length=100)
    var_descripcion = models.TextField()
    var_fk_tipo_ficha = models.ForeignKey(Tipo_equipo, on_delete=SET_NULL, null=True )


def __str__(self):
    return self.var_nombre
