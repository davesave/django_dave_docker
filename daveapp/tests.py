import time

from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.test import Client, TestCase


class DaveAppTests(TestCase):
    def test_dave_app_1(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertIsInstance(response, HttpResponse)
        time.sleep(10)  # to see the docker temporary container running and terminating
        self.assertEqual(response.status_code, 200)
