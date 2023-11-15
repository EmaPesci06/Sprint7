from django.shortcuts import render

# Create your views here.
def cuentas_templates(request):
    return render(request, 'cuentas/cuentas.html')