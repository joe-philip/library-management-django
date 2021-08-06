from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('activate/<int:id>', views.activate, name='activate'),
    path('deactivate/<int:id>', views.deactivate, name='deactivate'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('changePassword', views.changePassword, name='changePassword')
]
