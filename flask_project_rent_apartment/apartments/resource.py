import json
from flask import request
from flask_restful import Resource, marshal_with

from db import db
from utils import check_login
from models import ApartmentModel

from apartments.marshal_structure import apartment_structure
from apartments.parser import apartment_parser


class Apartment(Resource):
    method_decorators = [check_login]

    @marshal_with(apartment_structure)
    def get(self, apartment_id=None):
        if apartment_id:
            return ApartmentModel.query. \
                get_or_404(apartment_id, description='Apartment not found')
        else:
            return ApartmentModel.query.all()

    def post(self):
        data = json.loads(request.data)
        new_apartment = ApartmentModel(**data)
        db.session.add(new_apartment)
        db.session.commit()
        return f"Successfully added the new apartment " \
                   f"{new_apartment.id}", 201

    def put(self, apartment_id):
        data = json.loads(request.data)
        apartment = ApartmentModel.query. \
            get_or_404(apartment_id, description='Apartment not found')
        for key, value in data.items():
            setattr(apartment, key, value)
        db.session.commit()
        return f"Successfully updated the apartment number {apartment_id}"

    def delete(self, apartment_id):
        apartment = ApartmentModel.query. \
            get_or_404(apartment_id, description='Apartment not found')
        db.session.delete(apartment)
        db.session.commit()
        return f"Successfully deleted the apartment number {apartment_id}"
