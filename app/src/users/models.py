from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """custom user"""
    email = models.EmailField(verbose_name="Почта", max_length=150, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
