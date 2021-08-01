from django.shortcuts import redirect, render
from MAIN.forms import registrationForm
from MAIN.functions import createAdmin

# Create your views here.


def home(request):
    createAdmin()
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


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
