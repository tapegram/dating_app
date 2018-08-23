from flask import Flask, request
from users.repo import FirebaseUserRepo
from users.user import User
import json


app = Flask(__name__)


@app.route('/api/users', methods=["POST"])
def create_user():
    user = User(**request.get_json())
    return json.dumps(FirebaseUserRepo().create(user))


@app.route('/api/users', methods=["GET"])
def get_all_users():
    users = FirebaseUserRepo().get_all()
    return json.dumps(users)
