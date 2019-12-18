import json

from flask import Blueprint, Response, request
from flask_restful import Resource, marshal_with

from rooms_bp.resource import Rooms, TABLE, pars_room, rooms_structure

rooms_api_bp = Blueprint('GetRooms', __name__)


class GetRooms(Resource):

    @marshal_with(rooms_structure)
    def get(self):
        number = pars_room.parse_args().get('number')
        status = pars_room.parse_args().get('status')
        get_rooms = {
            "number": [room for room in TABLE if number == room.number],
            "status": [room for room in TABLE if status == room.status]
        }

        for key, value in pars_room.parse_args().items():
            if value is not None:
                return get_rooms.get(key)
        else:
            return TABLE

    def post(self):
        data = json.loads(request.data)
        number = data.get('number')
        price = data.get('price')
        level = data.get('level')
        status = data.get('status')

        if None in [number, level, status, price]:
            return Response("You must fill in the room information:"
                            " number, level, status, price", 412)
        try:
            number = int(data.get('number'))
            price = int(data.get('price'))
            level = int(data.get('level'))
        except ValueError:
            return Response("Room number, price and level"
                            " must be a number", 412)

        if str(number) in [str(room.number) for room in TABLE]:
            return Response("This room is already exist", 412)
        if number > 0:
            if price > 0:
                if status in ['Free', 'Tenanted']:
                    new_room = Rooms(**data)
                    TABLE.append(new_room)
                    return Response(f"Room {number} was added", 201)
                return Response("Status can be Free or Tenanted", 412)
            return Response("Price can't be negative", 412)
        return Response("Room number can't be negative", 412)

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

    def delete(self, room_number):
        if room_number in [room.number for room in TABLE]:
            [TABLE.remove(room) for room in TABLE
             if room.number == room_number]
            return f"Room {room_number} was deleted"
        else:
            return Response("This room doesn't exist", 412)
