from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Users must have an email or phone number address")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class OTP(models.Model):
    username = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    creat_at = models.DateTimeField(auto_now_add=True)
    last_send = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username