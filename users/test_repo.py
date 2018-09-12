from dating_app.users.repo import (
    IUserDataClient,
    UserRepo,
)
from dating_app.users.user import User
from unittest import TestCase


class DummyClient(IUserDataClient):
    def __init__(self):
        self.get_called = 0
        self.get_all_called = 0
        self.create_called = 0
        self.delete_called = 0
        self.delete_called_with = None

    def get(self, id):
        self.get_called += 1
        return {
            "username": "username",
            "first_name": "first",
            "last_name": "last",
        }

    def get_all(self):
        self.get_all_called += 1
        return {
            "id": {
                "username": "username",
                "first_name": "first",
                "last_name": "last",
            },
        }

    def create(self, user):
        self.create_called += 1

    def delete(self, user_id):
        self.delete_called += 1
        self.delete_called_with = user_id


class TestRepo(TestCase):

    def test_get_all(self):
        client = DummyClient()
        repo = UserRepo(client)
        users = repo.get_all()

        self.assertEqual(len(users), 1)

        user = users[0]
        self.assertIsInstance(user, User)

        user_json = user.to_json()
        self.assertEqual(user_json["id"], "id")
        self.assertEqual(user_json["username"], "username")
        self.assertEqual(user_json["first_name"], "first")
        self.assertEqual(user_json["last_name"], "last")

        self.assertEqual(client.get_all_called, 1)

    def test_create(self):
        client = DummyClient()
        repo = UserRepo(client)

        user = User(
            id="123",
            username="username",
            first_name="first",
            last_name="last")

        repo.create(user)

        self.assertEqual(client.create_called, 1)

    def test_get(self):
        client = DummyClient()
        repo = UserRepo(client)
        user = repo.get("user_id")

        self.assertIsInstance(user, User)

        user_json = user.to_json()
        self.assertEqual(user_json["id"], "user_id")
        self.assertEqual(user_json["username"], "username")
        self.assertEqual(user_json["first_name"], "first")
        self.assertEqual(user_json["last_name"], "last")

        self.assertEqual(client.get_called, 1)

    def test_delete(self):
        client = DummyClient()
        repo = UserRepo(client)
        repo.delete("deletetest")

        self.assertEqual(client.delete_called, 1)
        self.assertEqual(client.delete_called_with, "deletetest")
        
