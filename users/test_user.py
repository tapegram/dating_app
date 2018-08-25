from dating_app.users.user import User
from unittest import TestCase


class TestUser(TestCase):
    def test_init(self):
        data = {
            "id": "123",
            "username": "username",
            "first_name": "first",
            "last_name": "last",
            "some_other_junk": "asdasd"
        }

        user = User(**data)

        self.assertDictEqual(
            user.to_json(),
            {
                "id": "123",
                "username": "username",
                "first_name": "first",
                "last_name": "last"
            })
