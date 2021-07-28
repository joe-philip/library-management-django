from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def about_us(request):
    return render(request, 'about.html')
