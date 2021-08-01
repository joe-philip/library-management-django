from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return HttpResponse('This is admin dashboard')
