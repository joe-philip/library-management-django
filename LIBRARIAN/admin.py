from django.contrib import admin
from LIBRARIAN.models import authors, publishers, book_category, books

# Register your models here.
admin.site.register(authors)
admin.site.register(publishers)
admin.site.register(book_category)
admin.site.register(books)
