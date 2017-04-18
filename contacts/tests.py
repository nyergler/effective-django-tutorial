from django.test import TestCase

from .models import Contact


class ContactTests(TestCase):
    """Contact model tests."""

    def test_str(self):

        contact = Contact(first_name='John', last_name='Smith')

        self.assertEquals(
            str(contact),
            'John Smith',
        )
