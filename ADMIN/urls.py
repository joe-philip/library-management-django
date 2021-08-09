from django.urls import path
from . import views

urlpatterns = [
    path('activate/<int:id>', views.activate, name='activate'),
    path('deactivate/<int:id>', views.deactivate, name='deactivate'),
    path('delete/<int:id>', views.delete, name='delete'),
]
