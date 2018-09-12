import json
from abc import ABCMeta, abstractmethod
from firebase import firebase

from dating_app.users.user import User


class IUserDataClient(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, user):
        pass


class FirebaseUserDataClient(IUserDataClient):
    FIREBASE_URL = "https://dating-app-206bc.firebaseio.com/rest"

    def __init__(self):
        self._firebase = firebase.FirebaseApplication(self.FIREBASE_URL, None)

    def get(self, id):
        return self._firebase.get("/users", id)

    def get_all(self):
        return self._firebase.get("/users", None)

    def create(self, user):
        return self._firebase.post("/users", user_json)


class UserRepo(object):
    def __init__(self, client):
        self._client = client

    def get(self, id):
        user_json = self._client.get(id)
        return User(id=id, **user_json)

    def get_all(self):
        users_json = self._client.get_all()

        return [
            User(id=id, **user_json)
            for id, user_json in users_json.items()
        ]

    def create(self, user):
        user_json = user.to_json()
        self._client.create(user_json)
