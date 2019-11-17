from flask import Blueprint
from flask_restful import Api
from users.resource import User

user = Blueprint("user", __name__)
api_user = Api(user)

api_user.add_resource(User, "/users", "/user/<int:user_id>")
