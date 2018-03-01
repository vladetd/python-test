from .APIInterface import APIInterface

import requests

# General implementaion of the github API
class GithubAPI(APIInterface):

    CONST_URL = "https://api.github.com"
    CONST_API_VERSION = "application/vnd.github.v3+json"

    def get(self, endpoint, params=None):
        try:
            return requests.get(
                self.CONST_URL + '/' + endpoint,
                headers={
                    'Accept' : self.CONST_API_VERSION
                },
                data=params
            ).json()
        except:
            print("Whoops. Something went wrong")

    def post(self):
        # @TODO
        pass

    def delete(self):
        # @TODO
        pass

    def put(self):
        # @TODO
        pass
