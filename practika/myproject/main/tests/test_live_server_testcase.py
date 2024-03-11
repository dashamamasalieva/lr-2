from unittest import skip
from django.test import LiveServerTestCase
from selenium import webdriver
from main.models import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@skip("test skip")
class NameFunctionalTest(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        super().setUp()

    def tearDown(self):
        self.selenium.quit()
        super().tearDown()

    def test_product_list_functional(self):
        # Create test data
        Service.objects.create(name='Имплант зуба')
        Service.objects.create(name='Консультация')

        # Simulate user interactions using Selenium
        self.selenium.get(self.live_server_url + '/service/')
        self.assertIn('Список Услуг', self.selenium.name)
        names = self.selenium.find_elements(By.TAG_NAME, 'td')
        self.assertEqual(len(names), 2)
        self.assertEqual(names[0].text, 'Реставрация')
        self.assertEqual(names[1].text, 'Удаление')