from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Cliente

class createUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['customer_name', 'customer_surname', "customer_dni", "tipo_cliente", "dob", "branch_id"]
        labels={
            'tipo_cliente' : 'Tipo de cliente'
        }