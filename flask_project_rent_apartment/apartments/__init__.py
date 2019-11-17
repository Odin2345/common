from flask import Blueprint
from flask_restful import Api
from apartments.resource import Apartment

apartment = Blueprint("apartment", __name__)
api_apartment = Api(apartment)

api_apartment.add_resource(Apartment,
                           "/apartments",
                           "/apartments/<int:apartment_id>")
