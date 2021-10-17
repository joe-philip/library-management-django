from django.urls import path
from LIBRARIAN import views

urlpatterns = [
    path('activate/<int:id>', views.activate, name='activate'),
    path('deactivate/<int:id>', views.deactivate, name='deactivate'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('add/<str:choice>', views.add, name='add'),
    path('view/<str:choice>', views.view, name='view')
]
