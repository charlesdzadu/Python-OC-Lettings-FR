"""
Application configuration for profiles.
"""
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """Configuration class for the profiles application."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
