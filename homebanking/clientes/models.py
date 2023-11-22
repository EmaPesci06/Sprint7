from django.db import models
from django.contrib.auth.models import User
from sucursal.models import Sucursal

class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200)
    customer_surname = models.CharField(max_length=200)
    customer_dni = models.CharField(max_length=10, db_column='customer_DNI')
    dob = models.DateField(blank=True, null=True)  
    branch = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    tipo_cliente = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
