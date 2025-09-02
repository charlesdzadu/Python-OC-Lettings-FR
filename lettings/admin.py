"""
Admin configuration for lettings application.
"""
from django.contrib import admin
from .models import Letting, Address


admin.site.register(Letting)
admin.site.register(Address)
