from MAIN.models import User


def createAdmin():
    if not User.objects.filter(email='admin@library.com').exists():
        User.objects.create_user(
            email='admin@library.com',
            first_name='Admin',
            account_type='admin',
            password='admin',
            is_superuser=1,
            is_staff=1
        ).save()


def getAdminDashboard(userObject):
    context = {
        'user': userObject
    }
    try:
        context['librarians'] = User.objects.filter(account_type='librarian')
    except:
        pass
    return context


def getLibrarianDashboard(userObject):
    context = {
        'user': userObject
    }
    try:
        context['students'] = User.objects.filter(account_type='student')
    except:
        pass
    return context
