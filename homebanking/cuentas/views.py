from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cuentas_templates(request):
    return render(request, 'cuentas/cuentas.html')