from django.db import models

from variable.models import Variable
from ficha.models import Ficha

from django.db.models import SET_NULL

# Create your models here.


class Detalle(models.Model):
    idDetalle = models.AutoField(primary_key=True)
    #det_fk_fichas = 
    det_fk_variable = models.ForeignKey(Variable, on_delete=SET_NULL, null=True)
    det_fk_ficha = models.ForeignKey(Ficha, on_delete=SET_NULL, null=True)
    det_valor =  models.TextField()


def __str__(self):
    return self.det_valor