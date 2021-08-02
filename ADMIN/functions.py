from MAIN.models import User


def getAdminDashboard(userObject):
    context = {
        'user': userObject,
    }
    return context
