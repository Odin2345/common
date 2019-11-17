import json
from flask import request
from flask_restful import Resource, marshal_with

from db import db
from utils import check_login
from models import UserModel

from users.marshal_structure import user_structure
from apartments.parser import apartment_parser


class User(Resource):
    #method_decorators = [check_login]

    @marshal_with(user_structure)
    def get(self, user_id=None):
        if user_id:
            return UserModel.query. \
                get_or_404(user_id, description='User not found')
        else:
            return UserModel.query.all()

    def post(self):
        data = json.loads(request.data)
        new_apartment = UserModel(**data)
        db.session.add(new_apartment)
        db.session.commit()
        return f"Successfully added the new apartment " \
                   f"{new_apartment.id}", 201
