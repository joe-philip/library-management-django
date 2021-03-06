from django.shortcuts import redirect
from django.http.response import HttpResponse
from ADMIN.decorators import checkAdmin
from MAIN.models import User

# Create your views here.


@checkAdmin
def activate(request, id):
    if request.session.has_key('email'):
        user = User.objects.get(email=request.session['email'])
        if user.account_type == 'admin':
            activateLibrarian = User.objects.filter(id=id)
            activateLibrarian.update(is_active=1)
            return redirect('/dashboard')
        else:
            return HttpResponse('Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse('Login to access this page<br><a href="/login">Go Home</a>')


@checkAdmin
def deactivate(request, id):
    if request.session.has_key('email'):
        user = User.objects.get(email=request.session['email'])
        if user.account_type == 'admin':
            deactivateLibrarian = User.objects.filter(id=id)
            deactivateLibrarian.update(is_active=0)
            return redirect('/dashboard')
        else:
            return HttpResponse('Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse('Login to access this page<br><a href="/login">Go Home</a>')


@checkAdmin
def delete(request, id):
    if request.session.has_key('email'):
        user = User.objects.get(email=request.session['email'])
        if user.account_type == 'admin':
            deleteLibrarian = User.objects.filter(id=id)
            deleteLibrarian.delete()
            return redirect('/dashboard')
        else:
            return HttpResponse('Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse('Login to access this page<br><a href="/login">Go Home</a>')
