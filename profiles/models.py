"""
Models for the profiles application.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model representing user profile information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles_profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """String representation of Profile."""
        return self.user.username
