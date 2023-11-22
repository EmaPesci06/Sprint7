from django.db import models

# Create your models here.
class Movimientos(models.Model):
    numero_cuenta = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    tipo_operacion = models.CharField(max_length=50, blank=True, null=True) 
    hora = models.TextField(blank=True, null=True)