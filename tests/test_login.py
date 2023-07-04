import pytest
import requests, json

class TestCreateUser:
    def test_login_valid(self):
        data = {
            'username': 'teste',
            'password': '123'
        }

        requests.post('http://127.0.0.1:8000/login/', data=json.dumps(data))

