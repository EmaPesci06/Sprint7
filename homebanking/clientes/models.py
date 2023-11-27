from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    TIPO_CLIENTE=[
        ('GOLD', 'Cliente Gold'),
        ('BLACK', 'Cliente Black'),
        ('CLASSIC', 'Cliente Classic'),
    ]
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200)
    customer_surname = models.CharField(max_length=200)
    customer_dni = models.CharField(max_length=8, db_column='customer_DNI')
    dob = models.DateField(blank=True, null=True)
    branch_id = models.IntegerField()
    tipo_cliente = models.CharField(max_length=10, choices=TIPO_CLIENTE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
