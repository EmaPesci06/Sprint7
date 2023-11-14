from django import forms

class LoginForm(forms.Form):
    name= forms.CharField(label="Nombre", required=True)
    surname= forms.CharField(label="Apellido", required=True)
    email= forms.EmailField(label="Email", required=True)