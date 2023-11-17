from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home_template(request):
    return render(request, 'home/home.html')