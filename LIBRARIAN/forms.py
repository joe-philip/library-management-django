from django import forms
from LIBRARIAN.models import authors, publishers, book_category, books


class newAuthorForm(forms.ModelForm):
    class Meta:
        model = authors
        fields = '__all__'


class newPublisherForm(forms.ModelForm):
    class Meta:
        model = publishers
        fields = '__all__'


class newBookCategoryForm(forms.ModelForm):
    class Meta:
        model = book_category
        fields = '__all__'


class newBookForm(forms.ModelForm):
    class Meta:
        model = books
        fields = '__all__'
