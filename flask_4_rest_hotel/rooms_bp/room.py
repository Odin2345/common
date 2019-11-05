from flask import Blueprint
from flask_restful import Resource, marshal_with

from rooms_bp.resource import Rooms, TABLE, pars_room, rooms_structure

rooms_api_bp = Blueprint('GetRooms', __name__)


class GetRooms(Resource):

    @marshal_with(rooms_structure)
    def get(self):
        get_rooms = {
            "number": [room for room in TABLE
                       if pars_room.parse_args().get('number') == room.number],
            "status": [room for room in TABLE
                       if pars_room.parse_args().get('status') == room.status]}

        for key, value in pars_room.parse_args().items():
            if value is not None:
                return get_rooms.get(key)
        else:
            return TABLE

    def post(self):
        room_number = pars_room.parse_args().get('number')
        for room in TABLE:
            if room.number == room_number:
                return f'Room {room.number} already added to system'
        TABLE.append(Rooms(room_number,
                           pars_room.parse_args().get('level'),
                           pars_room.parse_args().get('status'),
                           pars_room.parse_args().get('price')))
        return f'Room {room_number} added to system', 201

    def put(self, room_number):
        for room in TABLE:
            if room.number == room_number:
                if pars_room.parse_args().get('level'):
                    room.level = pars_room.parse_args().get('level')
                if pars_room.parse_args().get('status'):
                    room.status = pars_room.parse_args().get('status')
                if pars_room.parse_args().get('price'):
                    room.price = pars_room.parse_args().get('price')
                return 'Information about room was updated', 200
        else:
            return 'Room not found', 404

    @marshal_with(rooms_structure)
    def delete(self, room_number):
        for room in TABLE:
            if room.number == room_number:
                TABLE.remove(room)
        return TABLE, 200
