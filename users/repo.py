from firebase import firebase


class IUserRepo(object):
    def get_all(self):
        pass

    def create(self, user):
        pass


class UserRepo(IUserRepo):
    FIREBASE_URL = "https://dating-app-206bc.firebaseio.com/rest"

    def __init__(self):
        self._firebase = firebase.FirebaseApplication(self.FIREBASE_URL, None)

    def get_all(self):
        users = self._firebase.get("/users", None)
        return users

    def create(self, user):
        user_json = user.to_json()
        return self._firebase.post("/users", user_json)
