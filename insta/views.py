from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})

# def login(request):
#     return render(request,'home.html')
# def logout_view(request):
#     logout(request)
#     return render(request, 'home.html')