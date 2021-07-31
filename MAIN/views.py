from django.shortcuts import render
from MAIN.forms import registrationForm

# Create your views here.


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def about_us(request):
    return render(request, 'about.html')


def contact_us(request):
    return render(request, 'contact.html')


def sign_up(request):
    context = {'form': registrationForm()}
    return render(request, 'signup.html', context)
