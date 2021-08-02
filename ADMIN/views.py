from django.shortcuts import render
from django.http.response import HttpResponse
from ADMIN.decorators import checkAdmin
from MAIN.models import User

# Create your views here.


@checkAdmin
def dashboard(request):
    if request.session.has_key('email'):
        user = User.objects.get(email=request.session['email'])
        if user.account_type == 'admin':
            return render(request, 'ADMIN/dashboard.html')
        else:
            return HttpResponse('Sorry you are not authorized to access this page<br><a href="/">Go Home</a>')
    else:
        return HttpResponse('Login to access this page<br><a href="/login">Go Home</a>')
