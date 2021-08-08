from django import forms
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

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        old_password = cleaned_data.get('old_password')
        current_user = User.objects.get(email=self.instance.email)
        if not current_user.check_password(old_password):
            raise forms.ValidationError('Incorrect old password')
        if new_password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        else:
            if len(new_password) < 8:
                raise forms.ValidationError(
                    'Minimum 8 characters required for password')

    class Meta:
        model = User
        fields = ('old_password', 'password', 'confirm_password')
        widgets = {'password': forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'New Password'})}
        labels = {
            'password': 'New Password'
        }
