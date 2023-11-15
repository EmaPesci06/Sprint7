from django.db import models

# Create your models here.

class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    id_tarjeta = models.IntegerField()
    brand = models.TextField()

    class Meta:
        managed = False
        db_table = 'marca'
