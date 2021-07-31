from django import forms
from MAIN.models import User


class registrationForm(forms.ModelForm):
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
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'style':'margin-right:1em'}),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email*',
                'margin':'0'}),
            'gender': forms.RadioSelect(),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone*'}),
            'password':forms.PasswordInput(attrs={'placeholder':'Password'})
        }
