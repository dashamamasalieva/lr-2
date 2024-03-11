from unittest import skip
from django.test import TestCase
from main.models import Service


class MyModelTest(TestCase):
    def setUp(self):
        self.object = Service.objects.create(ind="5")

    def test_str_representation(self):
        self.assertEqual(str(self.object), '5')

    def tearDown(self):
        pass
