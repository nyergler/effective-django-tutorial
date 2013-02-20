"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from contacts.models import Contact


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class ContactTests(TestCase):
    """Contact model tests."""

    def test_str(self):

        contact = Contact(first_name='John', last_name='Smith')

        self.assertEquals(
            str(contact),
            'John Smith',
        )
