from MAIN.models import User


def getAdminDashboard(userObject):
    context = {
        'user': userObject
    }
    try:
        context['librarians']=User.objects.filter(account_type='librarian')
    except:
        pass
    return context
