import requests
from zomato_api.endpoint_manager import EndpointManager
from zomato_api.custom_exceptions import *


class Requester(EndpointManager):
    def __init__(self, API_KEY=""):
        super().__init__()
        self.API_KEY = API_KEY
        self.headers = {'user-key': self.API_KEY}
        self.r = object

    def get(self, endpoint_name, payload=None):
        if payload is None:
            payload = {}
        url = self.endpoints[endpoint_name]
        self.r = requests.get(url, params=payload, headers=self.headers)
        self.check_for_exceptions(self.r)
        return self.r.json()

    @staticmethod
    def check_for_exceptions(request):
        status_code = request.status_code
        if status_code == 200:
            return
        elif status_code == 400:
            raise InvalidInputException("Invalid input")
        elif status_code == 404:
            raise NotFoundException("Not Found")
        elif status_code == 403:
            raise InvalidAPIKEYException("Invalid API KEY")
        else:
            raise ConnectionErrorException("The website couldn't be retrieved.")
