from django.shortcuts import render

# Create your views here.
def movimientos_template(request):
    return render(request, 'movimientos/movimientos.html')