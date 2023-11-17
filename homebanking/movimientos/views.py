from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def movimientos_template(request):
    return render(request, 'movimientos/movimientos.html')