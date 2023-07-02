import pytest
import requests, json

class TestCreateUser:
    def test_read_user_valid(self):
        result = requests.get(f'http://127.0.0.1:8000/users/')
        result_message = json.loads(result.content)

        assert result.status_code == 200
        assert all(key=='user' for key in result_message.keys())

