from dating_app.app import app, set_user_client
from dating_app.users.repo import IUserDataClient
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
            "id1": {
                "username": "username",
                "first_name": "first",
                "last_name": "last",
            },
            "id2": {
                "username": "rossing",
                "first_name": "ross",
                "last_name": "ingram",
            },
        }

    def create(self, user):
        self.create_called += 1

    def delete(self, user_id):
        self.delete_called += 1
        self.delete_called_with = user_id


class TestApp(TestCase):
    def setUp(self):
        self.app = app.test_client()
        set_user_client(DummyClient())

    def test_create_user(self):
        pass

    def test_get_all_users(self):
        resp = self.app.get('/api/users')
        resp_json = resp.get_json()

        self.assertEqual(len(resp_json), 2)

        users = sorted(resp_json, key=lambda x: x.get("id"))
        user1 = users[0]
        user2 = users[1]

        self.assertDictEqual(
            user1,
            {
                "first_name": "first",
                "last_name": "last",
                "username": "username",
                "id": "id1"
            })
        self.assertDictEqual(
            user2,
            {
                "first_name": "ross",
                "last_name": "ingram",
                "username": "rossing",
                "id": "id2"
            })

    def test_get_user(self):
        pass

    def test_delete_user(self):
        pass
