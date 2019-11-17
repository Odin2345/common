import json
from flask import request
from flask_restful import Resource, marshal_with

from db import db
from utils import check_login
from models import ApartmentModel

from apartments.marshal_structure import apartment_structure
from apartments.parser import apartment_parser


class SearchApartment(Resource):
    method_decorators = [check_login]

    @marshal_with(apartment_structure)
    def get(self):
        args = apartment_parser.parse_args()
        if any(args.values()):
            if args['price']:
                return ApartmentModel.query.filter_by(price=args['price']).all()
            elif args['city']:
                return ApartmentModel.query.filter_by(city=args['city']).all()
            elif args['rooms']:
                return ApartmentModel.query.filter_by(rooms=args['rooms']).all()
            elif args['district']:
                return ApartmentModel.query.filter_by(district=args['district']).all()







        if args:
            price = args.get("price")
            print(price)
            print(args['city'])
            rooms = args.get("rooms")
            city = args.get("city")
            district = args.get("district")
            from_the_owner = args.get("from_the_owner")

        # data = ApartmentModel.query.filter_by(city=city).all()
        return ApartmentModel.query.filter_by(city="Kyiv").all()
