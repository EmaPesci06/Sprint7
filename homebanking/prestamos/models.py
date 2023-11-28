# prestamos/models.py
from django.db import models
from django.contrib.auth.models import User
from .utils import obtener_tipo_cliente, obtener_limite_preaprobacion

class SolicitudPrestamo(models.Model):
    TIPOS_DE_PRESTAMO = [
        ('Hipotecario', 'Préstamo Hipotecario'),
        ('Prendario', 'Préstamo Prendario'),
        ('Personal', 'Préstamo Personal'),
    ]

    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_prestamo = models.CharField(max_length=20, choices=TIPOS_DE_PRESTAMO)
    fecha_inicio = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    aprobada = models.BooleanField(null=True, blank=True)

    def save(self, *args, **kwargs):
        tipo_cliente = obtener_tipo_cliente(self.cliente)
        limite_preaprobacion = obtener_limite_preaprobacion(tipo_cliente)

        if self.monto > limite_preaprobacion:
            self.aprobada = False
        else:
            self.aprobada = True
        super().save(*args, **kwargs)
