from django.shortcuts import render

# Create your views here.
def prestamos_template(request):
    return render(request, 'prestamos/prestamos.html')