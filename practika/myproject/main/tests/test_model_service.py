from django.test import TestCase
from main.models import Service


class ServiceModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Service.objects.create(name='Реставрация', price='100', ind="2")

    def test_first_name_label(self):
        service = Service.objects.get(id=1)
        field_label = service._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Имя')

    def test_phone_label(self):
        service = Service.objects.get(id=1)
        field_label = service._meta.get_field('ind').verbose_name
        self.assertEqual(field_label, 'Индекс')

    def test_surname_max_length(self):
        service = Service.objects.get(id=1)
        max_length = service._meta.get_field('price').max_length
        self.assertEqual(max_length, 50)

    def test_get_absolute_url(self):
        service = Service.objects.get(id=1)
        self.assertEqual(service.get_absolute_url(), 'service/1')
