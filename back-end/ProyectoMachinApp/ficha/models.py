from django.db import models

from tipoEquipo.models import Tipo_equipo

from django.db.models import SET_NULL
# Create your models here.
estadoFicha = (
    ('Operacion', 'Operacion'),
    ('fuera_de_servicio', 'fuera_de_servicio'),
    ('En_reparacion', 'En_reparacion'),
)

class Ficha(models.Model):
    idFichas = models.AutoField(primary_key=True)
    fi_fecha = models.DateField()
    fi_placa_sena = models.CharField(max_length=100)
    fi_serial = models.CharField(max_length=100)
    fi_fecha_adquisicion = models.DateField()
    fi_fecha_inicioGarantia = models.DateField()
    fi_fecha_finGarantia = models.DateField()
    fi_descripcionGarantia = models.TextField()
    fi_imagen = models.CharField(max_length=100)
    fi_estado = models.CharField(choices= estadoFicha, max_length=20)
    fi_fk_tipoFicha = models.ForeignKey(Tipo_equipo, on_delete=SET_NULL, null=True )
    #fi_fk_sitios


