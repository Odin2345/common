from flask_restful import fields

from rooms.marshal_structure import rooms_structure

tenants_structure = {
    'passport_id': fields.String,
    'name': fields.String,
    'age': fields.Integer,
    'sex': fields.String,
    'city': fields.String,
    'address': fields.String,
    'rooms': fields.Nested(rooms_structure)
}
