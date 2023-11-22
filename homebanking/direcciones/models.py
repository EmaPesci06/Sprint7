from django.db import models
from clientes.models import Cliente
from sucursal.models import Sucursal
from empleado.models import Empleado
# Create your models here.

class Direcciones(models.Model):
    address = models.OneToOneField(Sucursal, models.DO_NOTHING, primary_key=True)
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    employee = models.ForeignKey(Empleado, models.DO_NOTHING)
    address_0 = models.TextField(db_column='address')  # Field renamed because of name conflict.
    country = models.TextField()