from . import session

class API(object):

    def __init__(self, id):
        self.id = id
        self.head{'Content-Type': 'application/json'}

    def user_info(self):
        path = 'https://shared-sandbox-api.marqeta.com/v3/users'.format(self.token)
        response = session.get(path)
        return response.json()

    @staticmethod
    def accepted_countries():
        path = 'https://shared-sandbox-api.marqeta.com/v3/acceptedcountries'
        response = session.get(path)
        return response.json()