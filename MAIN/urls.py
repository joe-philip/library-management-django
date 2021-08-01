from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('sign_up', views.sign_up, name='sign_up')
]
