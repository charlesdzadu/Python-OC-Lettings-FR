"""
Application configuration for lettings.
"""
from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """Configuration class for the lettings application."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lettings'
