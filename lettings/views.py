"""
Views for the lettings application.
"""
import logging
from django.shortcuts import render, get_object_or_404
from .models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """
    Display list of all lettings.

    Args:
        request: HTTP request object

    Returns:
        Rendered lettings index page with list of all lettings
    """
    try:
        lettings_list = Letting.objects.all()
        logger.info(f"Lettings index accessed. Found {lettings_list.count()} lettings.")
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error(f"Error in lettings index: {str(e)}")
        raise


def letting(request, letting_id):
    """
    Display details of a specific letting.

    Args:
        request: HTTP request object
        letting_id: ID of the letting to display

    Returns:
        Rendered letting detail page
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        logger.info(f"Letting detail accessed: {letting.title} (ID: {letting_id})")
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        logger.warning(f"Letting not found: ID {letting_id}")
        raise
    except Exception as e:
        logger.error(f"Error accessing letting {letting_id}: {str(e)}")
        raise
