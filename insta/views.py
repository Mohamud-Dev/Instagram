from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required(login_url='/accounts/login/')

def register(request):
    return render(request,'django_registration/registration_form.html')
