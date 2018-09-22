from flask import Flask, request, jsonify
from dating_app.users.repo import FirebaseUserDataClient, UserRepo
from dating_app.users.user import User
import json


app = Flask(__name__)

class DB(object):

    def __init__(self):
        self.user_client = FirebaseUserDataClient()

db = DB()

def set_user_client(client):
    db.user_client = client


@app.route('/api/users', methods=["POST"])
def create_user():
    user = User(**request.get_json())
    repo = UserRepo(db.user_client)

    return json.dumps(repo.create(user))


@app.route('/api/users', methods=["GET"])
def get_all_users():
    repo = UserRepo(db.user_client)
    users = repo.get_all()

    users_json = [
        user.to_json() for user in users
    ]

    return jsonify(users_json)

@app.route('/api/users/<user_id>', methods=["GET"])
def get_user(user_id):
    repo = UserRepo(db.user_client)
    user = repo.get(user_id)

    return json.dumps(user.to_json())

@app.route('/api/users/<user_id>', methods=["DELETE"])
def delete_user(user_id):
    repo = UserRepo(db.user_client)
    user = repo.delete(user_id)

    return "Success"
