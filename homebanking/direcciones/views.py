from django.shortcuts import render

# Create your views here.
def direcciones_template(request):
    return render(request, 'direcciones/direcciones.html')