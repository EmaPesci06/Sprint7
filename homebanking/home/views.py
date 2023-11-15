from django.shortcuts import render

# Create your views here.
def home_template(request):
    return render(request, 'home/home.html')