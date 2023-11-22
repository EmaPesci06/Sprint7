# registration/views.py
from django.shortcuts import render, redirect
from .forms import RegistroFormulario

def registro_usuario(request):
    if request.method == 'POST':
        formulario = RegistroFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')  # Cambia 'exito_registro' por la URL de tu página de éxito
    else:
        formulario = RegistroFormulario()

    return render(request, 'registration/register.html', {'formulario': formulario})
