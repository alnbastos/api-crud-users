import pytest
import requests, json

class TestCreateUser:
    def test_create_user_valid(self):
        data = {
            'username': 'test',
            'email': 'test@test.com',
            'password': '123',
            'role': 'admin',
        }

        result = requests.post('http://127.0.0.1:8000/users/', data=json.dumps(data))

        assert result.status_code == 200
