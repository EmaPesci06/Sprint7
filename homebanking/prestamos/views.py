# prestamos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SolicitudPrestamoForm
from .models import SolicitudPrestamo
from .utils import obtener_tipo_cliente, obtener_limite_preaprobacion

@login_required
def solicitud_prestamo(request):
    if request.method == 'POST':
        form = SolicitudPrestamoForm(request.POST, user=request.user)

        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.cliente = request.user
            tipo_cliente = obtener_tipo_cliente(request.user)
            monto_preaprobado = obtener_limite_preaprobacion(tipo_cliente)

            # Verificar si el monto ingresado es mayor que el monto preaprobado
            monto_ingresado = form.cleaned_data['monto']
            if monto_ingresado > monto_preaprobado:
                messages.warning(request, 'Monto ingresado excede el límite preaprobado.')
                return render(request, 'prestamos/solicitud_prestamo.html', {'form': form})

            # Implementar la lógica para actualizar préstamo y saldo de la cuenta
            # ...

            solicitud.save()
            messages.success(request, 'Solicitud enviada con éxito.')
            return redirect('detalle_prestamo', pk=solicitud.pk)  # Redirige a la página de detalle del préstamo
    else:
        form = SolicitudPrestamoForm(user=request.user)

    return render(request, 'prestamos/solicitud_prestamo.html', {'form': form})

@login_required
def detalle_prestamo(request, pk):
    prestamo = get_object_or_404(SolicitudPrestamo, pk=pk)
    return render(request, 'prestamos/detalle_prestamo.html', {'prestamo': prestamo})
