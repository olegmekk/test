import requests


class Base:
    def __init__(self):
        self.user = "hello@world.com"
        self.password = "12345678"
        self.mainUrl = "https://google.com/"
        self.headers = {"content-type": "application/json"}
