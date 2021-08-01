from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from MAIN.forms import registrationForm, loginForm
from MAIN.functions import createAdmin
from MAIN.models import User
from MAIN.decorators import unauthenticatedUser

# Create your views here.


def home(request):
    createAdmin()
    return render(request, 'index.html')


@unauthenticatedUser
def login(request):
    context = {'form': loginForm}
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


def dashboard(request):
    if request.session.has_key('email'):
        user_active = User.objects.get(email=request.session['email'])
        if user_active.account_type == 'admin':
            return redirect('/ADMIN/dashboard')
        else:
            return redirect('/logout')
    else:
        context = {
            'form': loginForm,
            'error': 'Login to access Dashboard page'
        }
        return render(request, 'login.html', context)


def about_us(request):
    return render(request, 'about.html')


def contact_us(request):
    return render(request, 'contact.html')


@unauthenticatedUser
def sign_up(request):
    context = {'form': registrationForm()}
    if request.method == 'POST':
        form = registrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/')
        else:
            context['error'] = form.errors
            return render(request, 'signup.html', context)
    else:
        return render(request, 'signup.html', context)
