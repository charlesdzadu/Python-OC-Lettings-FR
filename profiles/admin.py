"""
Admin configuration for profiles application.
"""
from django.contrib import admin
from .models import Profile


admin.site.register(Profile)
