from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm

# Create your views here.
def user_login(request):

    login_form= LoginForm()

    if request.method=="POST":
        login_form= LoginForm(data=request.POST)

        if login_form.is_valid():
            name=request.POST.get('name')
            surname=request.POST.get('surname')
            email=request.POST.get('email')
        
        return redirect(reverse('login')+"?ok")

    return render(request,'login/login.html', {'login':login_form})