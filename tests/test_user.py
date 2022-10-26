import json
import random

import requests


class TestRegisterUserAPI:
    baseurl = "https://stores-tests-api.herokuapp.com/register"

    username = "user" + str(random.randint(1, 100))
    password = "password" + str(random.randint(1, 100))

    def test_successful_registration(self):
        response = requests.post(url=self.baseurl, json=json.loads(
            '{''"username": "user' + str(random.randint(1, 100)) + '", ''"password": "password' + str(
                random.randint(1, 100)) + '"}'
        ))
        assert response.status_code == 201
        assert response.json().get('message') == 'User created successfully.'
        assert response.json().get('uuid')

    def test_unsuccessful_registration(self):
        json_user = json.loads('{''"username": "' + self.username + '"}')
        json_password = json.loads('{''"password": "' + self.password + '"}')

        response_without_password = requests.post(url=self.baseurl, json=json_user)
        response_without_username = requests.post(url=self.baseurl, json=json_password)
        assert response_without_password.status_code == 400
        assert response_without_password.json().get('message') == {"password": "This field cannot be blank."}
        assert response_without_username.json().get('message') == {"username": "This field cannot be blank."}


class TestLoginUserAPI:
    baseurl = "https://stores-tests-api.herokuapp.com/auth"
    body = '{''"username": "user' + str(random.randint(1, 100)) + '", ''"password": "password' + str(
        random.randint(1, 100)) + '"}'

    def test_registration_user(self):
        response = requests.post(url="https://stores-tests-api.herokuapp.com/register", json=json.loads(self.body))
        assert response.status_code == 201

    def test_successful_auth(self):
        response = requests.post(url=self.baseurl, json=json.loads(self.body))
        assert response.status_code == 200
        assert type(response.json().get('access_token')) == str
