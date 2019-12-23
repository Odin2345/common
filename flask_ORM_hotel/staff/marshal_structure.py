from flask_restful import fields

from rooms.marshal_structure import rooms_structure

staff_structure = {
    'passport_id': fields.String,
    'name': fields.String,
    'position': fields.String,
    'salary': fields.Integer,
    'rooms': fields.Nested(rooms_structure)
}
