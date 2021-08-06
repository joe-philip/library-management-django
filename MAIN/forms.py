from django import forms
from django.forms import fields, widgets
from MAIN.models import User


class registrationForm(forms.ModelForm):
    account_type_choices = [
        ('student', 'Student'),
        ('librarian', 'Librarian')
    ]
    account_type = forms.ChoiceField(choices=account_type_choices)

    class Meta:
        model = User
        fields = ('first_name',
                  'middle_name',
                  'last_name',
                  'email',
                  'gender',
                  'phone',
                  'account_type',
                  'profile_pic',
                  'password')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name*',
                'required': ''}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email*',
                'margin': '0'}),
            'gender': forms.RadioSelect(),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone*'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }


class loginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'login-username',
        'placeholder': 'Email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'login-password',
            'placeholder': 'Password'}))


class editProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name',
                  'middle_name',
                  'last_name',
                  'email',
                  'gender',
                  'phone',
                  'profile_pic')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name*',
                'required': '',
                'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Middle Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email*',
                'margin': '0',
                'class': 'form-control',
                'readonly': ''}),
            'gender': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone*', 'class': 'form-control'})
        }


class changePasswordForm(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Old Passowrd'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Re-enter Passowrd'}))

    class Meta:
        model = User
        fields = ('password',)
        widgets = {'password': forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'New Password'}), }
