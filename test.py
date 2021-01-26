from unittest import TestCase
from app import app
from flask import session

class FlaskTest(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True


    def test_base(self)

        with self.client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertIn(country)
            self.assertIn('<form action="/get" method="POST">', html)
    
    def test_get_convert(self):
        with app.test_client() as client:
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 302)
