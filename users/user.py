class User(object):
    def __init__(self,
                 id=None,
                 username=None,
                 first_name=None,
                 last_name=None,
                 **kwargs):
        self._id = id
        self._username = username
        self._first_name = first_name
        self._last_name = last_name

    def to_json(self):
        return {
            "id": self._id,
            "username": self._username,
            "first_name": self._first_name,
            "last_name": self._last_name
        }
