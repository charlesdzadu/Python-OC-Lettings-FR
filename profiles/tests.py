"""
Tests for the profiles application.
"""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class ProfileModelTest(TestCase):
    """Test cases for Profile model."""

    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Paris'
        )

    def test_profile_str(self):
        """Test string representation of Profile."""
        self.assertEqual(str(self.profile), 'testuser')

    def test_profile_favorite_city(self):
        """Test favorite city field."""
        self.assertEqual(self.profile.favorite_city, 'Paris')


class ProfileViewsTest(TestCase):
    """Test cases for profile views."""

    def setUp(self):
        """Set up test client and data."""
        self.client = Client()
        self.user = User.objects.create_user(
            username='viewuser',
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            password='pass123'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='London'
        )

    def test_profiles_index_view(self):
        """Test profiles index view."""
        url = reverse('profiles:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'viewuser')
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_profile_detail_view(self):
        """Test profile detail view."""
        url = reverse('profiles:profile', kwargs={'username': 'viewuser'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'viewuser')
        self.assertContains(response, 'London')
        self.assertContains(response, 'John')
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_detail_view_not_found(self):
        """Test profile detail view with non-existent username."""
        url = reverse('profiles:profile', kwargs={'username': 'nonexistent'})
        with self.assertRaises(Profile.DoesNotExist):
            self.client.get(url)
