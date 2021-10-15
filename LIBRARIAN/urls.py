from django.urls import path
from LIBRARIAN import views

urlpatterns = [
    path('activate/<int:id>', views.activate, name='activate'),
    path('deactivate/<int:id>', views.deactivate, name='deactivate'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('addAuthor', views.addAuthor, name='addAuthor'),
    path('addPublisher', views.addPublisher, name='addPublisher'),
    path('addCategory', views.addCategory, name='addCategory'),
    path('addBook', views.addBook, name='addBook')
]
