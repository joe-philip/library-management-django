from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, unique=True)
    gender_choices = [
        ('Male', 'M'),
        ('Female', 'F')
    ]
    gender = models.CharField(max_length=50, choices=gender_choices)
    phone = models.PhoneNumberField(null=True)
    account_type_choices = [
        ('Admin', 'admin'),
        ('Librarian', 'librarian'),
        ('Student', 'student'),
    ]
    account_type = models.CharField(
        max_length=50,
        choices=account_type_choices,
        default=account_type_choices[2]
    )
    profile_pic = models.ImageField(
        upload_to=f'profilePics/{str(id)}/', null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.id
