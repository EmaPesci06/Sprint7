from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Cliente
from .forms import createUserForm, ClienteForm

def register(request):
    form = createUserForm
    cliente_form = ClienteForm

    if request.method == 'POST':
        form = createUserForm(request.POST)
        cliente_form = ClienteForm(request.POST)

        if form.is_valid() and cliente_form.is_valid():
            user = form.save()

            cliente = cliente_form.save(commit=False)
            cliente.usuario = user

            cliente.save()

            messages.success(request, 'Cuenta creada exitosamente')

            return redirect('login')

    context = {'form': form, 'cliente_form': cliente_form}
    return render(request, 'Clientes/register.html', context)