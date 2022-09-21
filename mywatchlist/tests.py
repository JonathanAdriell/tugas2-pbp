from django.test import TestCase
from django.test import Client
from django.urls import reverse

class MyWatchListTesting(TestCase):
    def setUp(self):
        self.client = Client()

    def test_url_html(self): # test show_mywatchlist
        response = self.client.get(reverse("mywatchlist:show_watchlist"))
        self.assertEqual(response.status_code, 200)
    
    def test_url_xml(self):
        response = self.client.get(reverse("mywatchlist:show_xml"))
        self.assertEqual(response.status_code, 200)

    def test_url_json(self):
        response = self.client.get(reverse("mywatchlist:show_json"))
        self.assertEqual(response.status_code, 200)