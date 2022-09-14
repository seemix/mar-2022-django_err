from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from apps.users.managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(150)])
    phone = models.CharField(max_length=10)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
