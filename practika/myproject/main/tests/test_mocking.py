from unittest import skip
from django.test import TestCase, RequestFactory
from unittest.mock import Mock, patch
from main.models import Service
from main.views import index


class ServiceListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_name_list_view(self):
        Service.objects.create(name='Реставрация')
        Service.objects.create(name='Удаление')

        request = self.factory.get('/index/')

        mock_queryset = Mock(spec=Service.objects.all())
        mock_queryset.return_value = [
            Mock(name='Реставрация'),
            Mock(name='Удаление')
        ]

        with patch('main.views.Service.objects.all', mock_queryset):
            response = index(request)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Реставрация')
        self.assertContains(response, 'Удаление')