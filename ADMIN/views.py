from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from ADMIN.decorators import checkAdmin
from ADMIN.functions import getAdminDashboard
from MAIN.models import User
from MAIN.forms import editProfileForm, changePasswordForm

# Create your views here.


@checkAdmin
def dashboard(request):
    if request.session.has_key('email'):
        user = User.objects.get(email=request.session['email'])
        if user.account_type == 'admin':
            context = getAdminDashboard(user)
            return render(request, 'ADMIN/dashboard.html', context)
        else:
            return HttpResponse('Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse('Login to access this page<br><a href="/login">Go Home</a>')


@checkAdmin
def activate(request, id):
    if request.session.has_key('email'):
        user = User.objects.get(email=request.session['email'])
        if user.account_type == 'admin':
            activateLibrarian = User.objects.filter(id=id)
            activateLibrarian.update(is_active=1)
            return redirect('/ADMIN/dashboard')
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
            return redirect('/ADMIN/dashboard')
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
            return redirect('/ADMIN/dashboard')
        else:
            return HttpResponse('Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse('Login to access this page<br><a href="/login">Go Home</a>')


@checkAdmin
def editprofile(request):
    if request.session.has_key('email'):
        user = User.objects.get(email=request.session['email'])
        if user.account_type == 'admin':
            context = {'editProfileForm': editProfileForm(instance=user)}
            if request.method == 'POST':
                formData = editProfileForm(
                    request.POST, request.FILES, instance=user)
                if formData.is_valid():
                    formData.save()
                    return redirect('/ADMIN/dashboard')
                else:
                    context['errors'] = formData.errors
                    return render(request, 'ADMIN/editprofile.html', context)
            else:
                return render(request, 'ADMIN/editprofile.html', context)
        else:
            return HttpResponse('Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse('Login to access this page<br><a href="/login">Go Home</a>')


@checkAdmin
def changePassword(request):
    if request.session.has_key('email'):
        user = User.objects.get(email=request.session['email'])
        if user.account_type == 'admin':
            if request.method == 'POST':
                formObj = changePasswordForm(request.POST, instance=user)
                if formObj.is_valid():
                    user = formObj.save()
                    user.set_password(formObj.cleaned_data['password'])
                    user.save()
                    return redirect('/logout')
            else:
                context = {
                    'changePasswordForm': changePasswordForm(instance=user)}
                return render(request, 'ADMIN/changepassword.html', context)
        else:
            return HttpResponse('Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse('Login to access this page<br><a href="/login">Go Home</a>')
