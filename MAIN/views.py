from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from MAIN.forms import registrationForm, loginForm
from MAIN.functions import createAdmin

# Create your views here.


def home(request):
    createAdmin()
    return render(request, 'index.html')


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
                return HttpResponse('Login Successfull')
            else:
                context['error'] = 'Invalid Credentials'
                return render(request, 'login.html', context)
        else:
            context['error']=form.errors
    else:
        return render(request, 'login.html', context)


def logout(request):
    if request.session.has_key('email'):
        request.session.flush()
    auth.logout(request)
    return redirect('/')


def about_us(request):
    return render(request, 'about.html')


def contact_us(request):
    return render(request, 'contact.html')


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
            print('Invalid')
            print(form.errors)
            context['error'] = form.errors
            return render(request, 'signup.html', context)
    else:
        return render(request, 'signup.html', context)
