import json
from flask_restful import Resource
from flask import session, request

from db import db
from auth.parser import auth_parser
from models import UserModel


class Login(Resource):
    def post(self):
        """
        Add to session new value logged_in = True and return success msg
        if news registered and put correct login and password
        :return: str
        """
        args = auth_parser.parse_args()#strict=True)
        email = args.get("email")
        password = args.get("password")
        data = UserModel.query.filter_by(email).first()

        if not data:
            return "There is no users in our system, please register", 401
        if email == data.email and password == data.password:
            session["logged_in"] = True
            return "You are successfully logged in"
        else:
            return "Wrong login or password", 403


class Logout(Resource):
    def get(self):
        """
        Change logged_in session value to False, which means that our decorator
        won't give access to see the page content from views where is it set.
        :return: str
        """
        session["logged_in"] = False
        return "You are successfully logged out"


class Registration(Resource):
    def post(self):
        """
        Add new news to dict news if he put all arguments
        :return:
        """
        data = json.loads(request.data)
        new_user = UserModel(**data)
        db.session.add(new_user)
        db.session.commit()
        return "Successfully registered"