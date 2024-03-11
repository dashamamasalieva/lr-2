from unittest import skip
from django.test import TransactionTestCase
from main.models import Service


@skip('Пропускаю тест ')
class WidgetTransactionTestCase(TransactionTestCase):
    def test_widget_creation(self):
        Service.objects.create(name='Отбеливание')
        Service.objects.create(name='Протезирование')
        self.assertEqual(Service.objects.count(), 2)