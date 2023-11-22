from django.db import models
from clientes.models import Cliente

# Create your models here.
class Tarjeta(models.Model):
    customer = models.ForeignKey(Cliente, models.DO_NOTHING)
    tarjeta_number = models.TextField()
    cvv = models.TextField()
    issuance_date = models.TextField()
    expiration_date = models.TextField()
    type = models.TextField()