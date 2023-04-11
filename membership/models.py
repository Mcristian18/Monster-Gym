from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
import uuid

# Create your models here.


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')
        
        return self.create_user(email, user_name, first_name, last_name, password, **other_fields)
    def create_user(self, email, user_name, first_name, last_name, password, **other_fields):

        if not email:
            raise ValueError('You must provide an email adress')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    def __str__(self):
        return self.user_name
    
# class VerifiedUsersManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_verified=True)
    

# class NotVerifiedUsersManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(is_verified=False)


class Monthly(models.Model):
    unique_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    full_name = models.CharField(max_length=150, blank=True)
    age = models.BigIntegerField(blank=True)
    adress = models.CharField(max_length=150, blank=True)
    contact_no = models.BigIntegerField(blank=True)
    email = models.EmailField(blank=True)
    weight = models.CharField(max_length=150, blank=True)
    height = models.CharField(max_length=150, blank=True)
    em_fullname = models.CharField(max_length=150, blank=True)
    relationship = models.CharField(max_length=150, blank=True)
    em_contactno = models.BigIntegerField(blank=True)
    em_email = models.EmailField(blank=True)
    file = models.FileField(blank=True)
    is_verified = models.BooleanField(default=False)
    start_date = models.DateTimeField(blank=True, null=True,)
    end_date = models.DateTimeField(blank=True, null=True,)

    # verified_objects = VerifiedUsersManager() 
    # nverified_objects = NotVerifiedUsersManager() 
    