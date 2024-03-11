from unittest import skip
from django.test import TestCase
from main.forms import ServiceForm


class FormTest(TestCase):
    def test_form_valid(self):
        form_data = {'name': 'стоматология',
                     "price": '100',
                     "ind": '11'}
        form = ServiceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {'name': '',
                     "price": '',
                     "ind": ''}
        form = ServiceForm(data=form_data)
        self.assertFalse(form.is_valid())