import logging

import requests

logger = logging.getLogger("api")


class RegisterUser:
    def __init__(self, url):
        self.url = url

    def register_user(self, body: dict):
        response = requests.post(url=self.url, json=body)
        # logger.info(response.text)
        return response.json()
