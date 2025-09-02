"""
Tests for the lettings application.
"""
from django.test import TestCase, Client
from django.urls import reverse
from .models import Address, Letting


class AddressModelTest(TestCase):
    """Test cases for Address model."""

    def setUp(self):
        """Set up test data."""
        self.address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TST"
        )

    def test_address_str(self):
        """Test string representation of Address."""
        self.assertEqual(str(self.address), "123 Test Street")

    def test_address_plural(self):
        """Test plural name of Address model."""
        self.assertEqual(Address._meta.verbose_name_plural, "Addresses")


class LettingModelTest(TestCase):
    """Test cases for Letting model."""

    def setUp(self):
        """Set up test data."""
        self.address = Address.objects.create(
            number=456,
            street="Another Street",
            city="Another City",
            state="AS",
            zip_code=67890,
            country_iso_code="AST"
        )
        self.letting = Letting.objects.create(
            title="Test Letting",
            address=self.address
        )

    def test_letting_str(self):
        """Test string representation of Letting."""
        self.assertEqual(str(self.letting), "Test Letting")


class LettingViewsTest(TestCase):
    """Test cases for lettings views."""

    def setUp(self):
        """Set up test client and data."""
        self.client = Client()
        self.address = Address.objects.create(
            number=789,
            street="View Street",
            city="View City",
            state="VS",
            zip_code=11111,
            country_iso_code="VST"
        )
        self.letting = Letting.objects.create(
            title="View Letting",
            address=self.address
        )

    def test_lettings_index_view(self):
        """Test lettings index view."""
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Letting")
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_letting_detail_view(self):
        """Test letting detail view."""
        url = reverse('lettings:letting', kwargs={'letting_id': self.letting.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Letting")
        self.assertContains(response, "View Street")
        self.assertTemplateUsed(response, 'lettings/letting.html')

    def test_letting_detail_view_not_found(self):
        """Test letting detail view with non-existent ID."""
        url = reverse('lettings:letting', kwargs={'letting_id': 9999})
        with self.assertRaises(Letting.DoesNotExist):
            self.client.get(url)
