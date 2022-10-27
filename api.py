import logging

import requests

from models import CreateUser

logger = logging.getLogger("api")


class RegisterUser:
    def __init__(self, url):
        self.url = url
        # self.uuid = None
        # self.access_token = None


    def register_user(self, body: dict):
        response = requests.post(url="https://stores-tests-api.herokuapp.com/register", json=body)
        logger.info(response.text)
        return response.json()




# body = CreateUser.create_user_password()
# user = RegisterUser(url="https://stores-tests-api.herokuapp.com/register").register_user(body)
# print(user["uuid"])