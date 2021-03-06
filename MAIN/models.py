from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class userManager(BaseUserManager):
    def create_user(self, first_name=None, middle_name=None, last_name=None, email=None, gender=None, phone=None, account_type=None, profile_pic=None, is_superuser=False, is_staff=False, is_active=True, password=None):
        if not email:
            raise ValueError('Email is a required field')
        if not password:
            raise ValueError('Blank passwords are not allowed')
        user = self.model()
        user.first_name = first_name
        user.middle_name = middle_name
        user.last_name = last_name
        user.email = self.normalize_email(email)
        user.gender = gender
        user.phone = phone
        user.account_type = account_type
        user.profile_pic = profile_pic
        user.is_superuser = is_superuser
        user.is_active = is_active
        user.is_staff = is_staff
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name=None, middle_name=None, last_name=None, password=None):
        user = self.create_user(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            password=password,
            account_type='librarian',
            is_staff=True
        )
        return user

    def create_superuser(self, email, first_name=None, middle_name=None, last_name=None, password=None):
        user = self.create_user(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            email=email,
            password=password,
            account_type='admin',
            is_staff=True,
            is_superuser=True
        )
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True,blank=True)
    email = models.EmailField(max_length=254, unique=True)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    gender = models.CharField(max_length=50, choices=gender_choices, null=True,blank=True)
    phone = models.CharField(max_length=20, null=True,blank=True)
    account_type_choices = [
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('student', 'Student')
    ]
    account_type = models.CharField(
        max_length=50,
        choices=account_type_choices,
        default=account_type_choices[2]
    )
    profile_pic = models.ImageField(
        upload_to=f'profilePics/', null=True, blank=True)
    date_joined = models.DateTimeField(auto_now=False, auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']
    objects = userManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def superuser_status(self):
        return self.is_superuser

    @property
    def staff_status(self):
        return self.is_staff

    @property
    def active_status(self):
        return self.is_active

    def __str__(self) -> str:
        return str(self.id)
