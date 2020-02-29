import os
import unittest
import json
from base64 import b64encode
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app=  app.test_client()
        self.assertEqual(app.debug,True)

    def tearDown(self):
        pass

    def get_api_headers(self, username, password):
        return {
            'Authorization': 'Basic ' + b64encode(
                (username + ':' + password).encode('utf-8')).decode('utf-8'),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def test_no_auth(self):
        response = self.app.get('/v1/weather',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_404(self):
        response = self.app.get('/no/url', headers=self.get_api_headers('weather','fintechfintech'))
        self.assertEqual(response.status_code, 404)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['error'], 'Not found')

    def test_melbourne(self):
        response = self.app.get('/v1/weather?city=melbourne', headers=self.get_api_headers('weather','fintechfintech'))
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['wind_speed'], 20)
        self.assertEqual(json_response['temperature_degrees'], 29)

if __name__ == '__main__':
    unittest.main()
