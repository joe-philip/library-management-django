from django.shortcuts import redirect
from django.http.response import HttpResponse
from MAIN.models import User

# Create your views here.


def activate(request, id):
    if 'email' in request.session:
        user = User.objects.get(email=request.session['email'])
        if user.account_type == User.account_type_choices[1][0]:
            activateLibrarian = User.objects.filter(id=id)
            activateLibrarian.update(is_active=1)
            return redirect('/dashboard')
        else:
            return HttpResponse(
                'Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse(
            'Login to access this page<br><a href="/login">Go Home</a>')


def deactivate(request, id):
    if 'email' in request.session:
        user = User.objects.get(email=request.session['email'])
        if user.account_type == User.account_type_choices[1][0]:
            deactivateLibrarian = User.objects.filter(id=id)
            deactivateLibrarian.update(is_active=0)
            return redirect('/dashboard')
        else:
            return HttpResponse(
                'Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse(
            'Login to access this page<br><a href="/login">Go Home</a>')


def delete(request, id):
    if 'email' in request.session:
        user = User.objects.get(email=request.session['email'])
        if user.account_type == User.account_type_choices[1][0]:
            deleteLibrarian = User.objects.filter(id=id)
            deleteLibrarian.delete()
            return redirect('/dashboard')
        else:
            return HttpResponse(
                'Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse(
            'Login to access this page<br><a href="/login">Go Home</a>')
