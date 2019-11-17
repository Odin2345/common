from flask_restful import fields

apartment_structure = {
    'id': fields.Integer,
    'city': fields.String,
    'district': fields.String,
    'rooms': fields.Integer,
    'price': fields.Integer,
    'owner': fields.String,
    'representative': fields.String
}
