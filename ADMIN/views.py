from django.http.response import HttpResponse
from ADMIN.decorators import checkAdmin

# Create your views here.


@checkAdmin
def dashboard(request):
    return HttpResponse('This is admin dashboard')
