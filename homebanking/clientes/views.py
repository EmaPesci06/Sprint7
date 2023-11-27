from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ClienteForm, createUserForm
from .models import Cliente

@login_required
def clientes_template(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes/cliente_template.html", {'clientes':clientes})



@login_required
def detalle_cliente(request, customer_id):
    cliente = Cliente.objects.get(pk=customer_id)
    return render(request, 'clientes/detalle_cliente.html', {'cliente': cliente})

@login_required
def register_page(request):
    form = createUserForm()
    profile_form = ClienteForm()

    if request.method == 'POST':
        form = createUserForm(request.POST)
        profile_form = ClienteForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            # No guardamos profile_form aquí porque primero debemos obtener el valor de profile_form,
            # asignar el usuario al OneToOneField creado en modelos antes de guardar profile_form.

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, 'Your account has been successfully created')

            return redirect('lista_clientes')

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'clientes/register.html', context)
