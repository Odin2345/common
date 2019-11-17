from flask_restful import reqparse

apartment_parser = reqparse.RequestParser(bundle_errors=True)
apartment_parser.add_argument('price', type=int, help='Price')
apartment_parser.add_argument('rooms', type=int, help='Rooms')
apartment_parser.add_argument('city', type=str, help='City')
apartment_parser.add_argument('district', type=str, help='District')
apartment_parser.add_argument('from_the_owner', type=bool, help='From_the_owner')
