from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def tarjetas_template(request):
    return render(request, 'tarjetas/tarjetas.html')