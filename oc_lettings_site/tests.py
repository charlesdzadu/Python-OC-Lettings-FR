"""
Tests for the main oc_lettings_site application.
"""
from django.test import TestCase, Client
from django.urls import reverse


class MainViewsTest(TestCase):
    """Test cases for main application views."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    def test_index_view(self):
        """Test homepage view."""
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to Holiday Homes')
        self.assertTemplateUsed(response, 'index.html')

    def test_index_contains_links(self):
        """Test that homepage contains links to lettings and profiles."""
        url = reverse('index')
        response = self.client.get(url)
        self.assertContains(response, 'href="{}"'.format(reverse('lettings:index')))
        self.assertContains(response, 'href="{}"'.format(reverse('profiles:index')))

    def test_404_page(self):
        """Test custom 404 page."""
        response = self.client.get('/nonexistent-page/')
        self.assertEqual(response.status_code, 404)
