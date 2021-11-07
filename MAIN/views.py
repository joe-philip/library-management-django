from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from MAIN.forms import registrationForm, loginForm, editProfileForm, changePasswordForm
from MAIN.functions import *
from MAIN.models import User
from MAIN.decorators import unauthenticatedUser

# Create your views here.


def home(request):
    createAdmin()
    return render(request, 'index.html')


def about_us(request):
    return render(request, 'about.html')


def contact_us(request):
    return render(request, 'contact.html')


@unauthenticatedUser
def login(request):
    context = {'form': loginForm()}
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = auth.authenticate(email=email, password=password)
            if user is not None:
                auth.login(request, user)
                request.session['email'] = email
                return redirect('/dashboard')
            else:
                context['error'] = 'Invalid Credentials'
                return render(request, 'login.html', context)
        else:
            context['error'] = form.errors
    else:
        return render(request, 'login.html', context)


def logout(request):
    if request.session.has_key('email'):
        request.session.flush()
    auth.logout(request)
    return redirect('/')


@login_required
def dashboard(request):
    if request.session.has_key('email'):
        user = User.objects.get(email=request.session['email'])
        if user.account_type == User.account_type_choices[0][0]:
            context = getAdminDashboard(user)
            return render(request, 'ADMIN/dashboard.html', context)
        elif user.account_type == User.account_type_choices[1][0]:
            context = getLibrarianDashboard(user)
            return render(request, 'LIBRARIAN/dashboard.html', context)
        elif user.account_type == User.account_type_choices[2][0]:
            return render(request, 'STUDENT/dashboard.html')
        else:
            return redirect('/logout')
    else:
        context = {
            'form': loginForm(),
            'error': 'Login to access Dashboard page'
        }
        return render(request, 'login.html', context)


@login_required
def editprofile(request):
    if request.session.has_key('email'):
        user = User.objects.get(email=request.session['email'])
        context = {'editProfileForm': editProfileForm(instance=user)}
        if request.method == 'POST':
            formData = editProfileForm(
                request.POST, request.FILES, instance=user)
            if formData.is_valid():
                formData.save()
                return redirect('/dashboard')
            else:
                context['errors'] = formData.errors
                return render(request, 'editprofile.html', context)
        else:
            return render(request, 'editprofile.html', context)
    else:
        return HttpResponse('Login to access this page<br><a href="/login">Go Home</a>')


@login_required
def changePassword(request):
    if request.session.has_key('email'):
        user = User.objects.get(email=request.session['email'])
        if user.account_type == 'admin':
            context = {'changePasswordForm': changePasswordForm(instance=user)}
            if request.method == 'POST':
                formObj = changePasswordForm(request.POST, instance=user)
                if formObj.is_valid():
                    user = formObj.save()
                    user.set_password(formObj.cleaned_data['password'])
                    user.save()
                    return redirect('/logout')
                else:
                    context['errors'] = formObj.errors
                    return render(request, 'changepassword.html', context)
            else:
                return render(request, 'changepassword.html', context)
        else:
            return HttpResponse('Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse('Login to access this page<br><a href="/login">Go Home</a>')


@login_required
def viewProfile(request):
    if request.session.has_key('email'):
        user = User.objects.get(email=request.session['email'])
        if user.account_type == 'admin':
            context = {
                'user': User.objects.get(email=request.session['email'])
            }
            return render(request, 'viewprofile.html', context)
        else:
            return HttpResponse('Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse('Login to access this page<br><a href="/login">Go Home</a>')


@unauthenticatedUser
def sign_up(request):
    context = {'form': registrationForm()}
    if request.method == 'POST':
        form = registrationForm(request.POST, request.FILES)
        if request.POST['account_type'] == 'student':
            if not User.objects.filter(account_type='librarian').exists():
                context['error'] = '''Sorry, We do not have any librarian staffs avialable to approve you registration... Registration could not be completed'''
                return render(request, 'signup.html', context)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.is_active = 0
            user.save()
            return redirect('/')
        else:
            context['error'] = form.errors
            return render(request, 'signup.html', context)
    else:
        return render(request, 'signup.html', context)
