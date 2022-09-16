from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

# Create your models here.
from apps.users.enums import RegEx
from apps.users.managers import UserManager
from apps.users.services import upload_to


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    password = models.CharField(max_length=128,
                                validators=[RegexValidator(RegEx.PASSWORD.pattern, RegEx.PASSWORD.message)])
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

    name = models.CharField(max_length=100, validators=[RegexValidator(RegEx.NAME.pattern, RegEx.NAME.message)])
    surname = models.CharField(max_length=100, validators=[RegexValidator(RegEx.NAME.pattern, RegEx.NAME.message)])
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(150)])
    phone = models.CharField(max_length=10, validators=[RegexValidator(RegEx.PHONE.pattern, RegEx.PHONE.message)])
    avatar = models.ImageField(upload_to=upload_to, blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
