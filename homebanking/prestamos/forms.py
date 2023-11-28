# prestamos/forms.py
from django import forms

from .utils import obtener_limite_preaprobacion, obtener_tipo_cliente
from .models import SolicitudPrestamo

class SolicitudPrestamoForm(forms.ModelForm):
    monto = forms.DecimalField(label='Monto Deseado del Préstamo', required=True)

    class Meta:
        model = SolicitudPrestamo
        fields = ['tipo_prestamo', 'fecha_inicio', 'monto']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user:
            tipo_cliente = obtener_tipo_cliente(user)
            monto_preaprobado = obtener_limite_preaprobacion(tipo_cliente)

            # Establecer el valor preaprobado y hacer el campo 'monto' readonly
            self.fields['monto'].initial = monto_preaprobado
            self.fields['monto'].widget.attrs['readonly'] = True
