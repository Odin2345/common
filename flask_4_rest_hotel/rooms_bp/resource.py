from flask_restful import fields, reqparse


class Rooms(object):
    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price


rooms_structure = {
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String,
    "price": fields.Integer}

pars_room = reqparse.RequestParser(bundle_errors=True)
pars_room.add_argument('number', type=int, help='Number of room must be int')
pars_room.add_argument('level', type=int, help='Level must be int')
pars_room.add_argument('status', type=str, help='Status is incorrect')
pars_room.add_argument('price', type=int, help='Price must be int')

TABLE = [Rooms(1, 1, 'Free', 850),
         Rooms(2, 1, 'Tenanted', 850),
         Rooms(3, 1, 'Tenanted', 700),
         Rooms(4, 1, 'Free', 700),
         Rooms(5, 2, 'Free', 650),
         Rooms(6, 2, 'Tenanted', 650),
         Rooms(7, 2, 'Free', 650),
         Rooms(8, 2, 'Tenanted', 650),
         Rooms(9, 3, 'Tenanted', 1000),
         Rooms(10, 3, 'Free', 1000)]
