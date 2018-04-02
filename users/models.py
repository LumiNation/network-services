"""Data models for all users."""
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """CustomUser Model used in case modifications required later."""
    def __str__(self):
        """Basic str representation of CustomUser."""
        return self.email

    name = models.CharField(blank=True, max_length=255)
