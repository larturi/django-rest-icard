from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email