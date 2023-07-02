import pytest
import requests, json

class TestCreateUser:
    def test_create_user_valid(self):
        user_id = '2'

        result = requests.get(f'http://127.0.0.1:8000/users/{user_id}')

        assert result.status_code == 200
