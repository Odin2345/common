from flask_restful import reqparse

auth_parser = reqparse.RequestParser(bundle_errors=True)
auth_parser.add_argument('email', required=True)
auth_parser.add_argument('password', required=True)
