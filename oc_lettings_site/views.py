"""
Views for the main oc_lettings_site application.
"""
from django.shortcuts import render


def index(request):
    """
    Display the homepage.

    Args:
        request: HTTP request object

    Returns:
        Rendered homepage
    """
    return render(request, 'index.html')


def custom_404(request, exception):
    """
    Custom 404 error page.

    Args:
        request: HTTP request object
        exception: Exception that triggered the 404

    Returns:
        Rendered 404 error page
    """
    return render(request, '404.html', status=404)


def custom_500(request):
    """
    Custom 500 error page.

    Args:
        request: HTTP request object

    Returns:
        Rendered 500 error page
    """
    return render(request, '500.html', status=500)
