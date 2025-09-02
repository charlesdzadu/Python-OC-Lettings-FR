"""
Views for the profiles application.
"""
import logging
from django.shortcuts import render, get_object_or_404
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """
    Display list of all profiles.

    Args:
        request: HTTP request object

    Returns:
        Rendered profiles index page with list of all profiles
    """
    try:
        profiles_list = Profile.objects.all()
        logger.info(f"Profiles index accessed. Found {profiles_list.count()} profiles.")
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        logger.error(f"Error in profiles index: {str(e)}")
        raise


def profile(request, username):
    """
    Display details of a specific user profile.

    Args:
        request: HTTP request object
        username: Username of the profile to display

    Returns:
        Rendered profile detail page
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
        logger.info(f"Profile accessed: {username}")
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist:
        logger.warning(f"Profile not found: {username}")
        raise
    except Exception as e:
        logger.error(f"Error accessing profile {username}: {str(e)}")
        raise
