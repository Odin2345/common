from flask import Blueprint
from flask_restful import Api
from search_apartment.resource import SearchApartment

search_apartment = Blueprint("search_apartment", __name__)
api_search_apartment = Api(search_apartment)

api_search_apartment.add_resource(SearchApartment, "/apartments/search")