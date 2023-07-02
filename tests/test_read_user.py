import pytest
import requests, json

class TestCreateUser:
    def test_read_user_valid(self):
        user_id = '2'

        result = requests.get(f'http://127.0.0.1:8000/users/{user_id}')

        assert result.status_code == 200


    def test_read_user_invalid(self):
        data_errors = ['1', None, 1, 'x', Exception]

        for data_error in data_errors:
            result = requests.get(f'http://127.0.0.1:8000/users/{data_error}')
            result_mensage = json.loads(result.content)

            assert result.status_code == 200
            assert result_mensage == {'user': 'User not exists.'}

