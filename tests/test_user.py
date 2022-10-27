import json
import logging

import requests

from api import RegisterUser
from models import CreateUser

logger = logging.getLogger("test_user")


class TestRegisterUserAPI:
    baseurl = "https://stores-tests-api.herokuapp.com/register"

    body = CreateUser.create_user_password()

    def test_successful_registration(self):
        response = requests.post(url=self.baseurl, json=self.body)
        assert response.status_code == 201
        assert response.json().get('message') == 'User created successfully.'
        assert response.json().get('uuid')
        logger.info(response.text)

    def test_unsuccessful_registration(self):
        json_user = json.loads('{"username": "username"}')
        json_password = json.loads('{"password": "password"}')
        response_without_password = requests.post(url=self.baseurl, json=json_user)
        response_without_username = requests.post(url=self.baseurl, json=json_password)
        assert response_without_password.status_code == 400
        assert response_without_password.json().get('message') == {"password": "This field cannot be blank."}
        assert response_without_username.json().get('message') == {"username": "This field cannot be blank."}
        logger.info(response_without_password.text)
        logger.info(response_without_username.text)


class TestLoginUserAPI:
    baseurl = "https://stores-tests-api.herokuapp.com/auth"

    body = CreateUser.create_user_password()
    user = RegisterUser(url=baseurl).register_user(body)

    def test_successful_auth(self):
        response = requests.post(url=self.baseurl, json=self.body)
        assert response.status_code == 200
        assert type(response.json().get('access_token')) == str


class TestUserInfoAPI:
    baseurl = "https://stores-tests-api.herokuapp.com/"
    body = CreateUser.create_user_password()
    user = RegisterUser(url=baseurl).register_user(body)

    def test_successful_add_user_info(self):
        user_auth = requests.post(url=self.baseurl + "auth", json=self.body)
        access_token = user_auth.json().get('access_token')
        headers = {"Authorization": "JWT " + access_token}
        js = json.loads(
            '{"phone": "string123",'
            '"email": "string123",'
            '"address": {"city": "string321", "street": "string555", "home_number": "string555"}}'
        )
        response = requests.post(url=f"{self.baseurl}user_info/{self.user['uuid']}", headers=headers, json=js)
        assert response.status_code == 200
        logger.info(response.text)

    def test_successful_get_user_info(self):
        user_auth = requests.post(url=self.baseurl + "auth", json=self.body)
        access_token = user_auth.json().get('access_token')
        headers = {"Authorization": "JWT " + access_token}
        response = requests.get(url=f"{self.baseurl}user_info/{self.user['uuid']}", headers=headers)
        assert response.status_code == 200
        logger.info(response.text)
