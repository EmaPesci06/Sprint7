from django.shortcuts import redirect, render

# Create your views here.
def tarjetas_template(request):
    return render(request, 'tarjetas/tarjetas.html')