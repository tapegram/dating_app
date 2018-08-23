from flask import Flask, request
from users.repo import UserRepo
from users.user import User
import json


app = Flask(__name__)


@app.route('/api/users', methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        user = User(**request.get_json())
        return json.dumps(UserRepo().create(user))
    else:
        users = UserRepo().get_all()
        return json.dumps(users)
