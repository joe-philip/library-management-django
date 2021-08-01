from django.http.response import HttpResponse
from django.shortcuts import redirect


def checkAdmin(view_function):
    def wrapper_function(request, *args, **kwargs):
        if hasattr(request.user, 'account_type'):
            if request.user.account_type == 'admin':
                return view_function(request, *args, **kwargs)
            else:
                return redirect('/')
        else:
            return HttpResponse('You are not authorized to view this page<br><a href="/">Go Home</a>')
    return wrapper_function
