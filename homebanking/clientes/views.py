from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import createUserForm, ClienteForm
from django.contrib.auth.decorators import login_required

@login_required
def cliente_template(request):
    return render(request, 'Clientes/register.html')