from flask import Flask, request
from users.repo import FirebaseUserDataClient, UserRepo
from users.user import User
import json


app = Flask(__name__)


@app.route('/api/users', methods=["POST"])
def create_user():
    user = User(**request.get_json())
    repo = UserRepo(FirebaseUserDataClient())

    return json.dumps(repo.create(user))


@app.route('/api/users', methods=["GET"])
def get_all_users():
    repo = UserRepo(FirebaseUserDataClient())
    users = repo.get_all()

    users_json = [
        user.to_json() for user in users
    ]

    return json.dumps(users_json)
