import json
from flask import request, Response
from flask_restful import Resource, marshal_with

from db import db
from utils import check_login
from models import RoomsModel
from rooms.marshal_structure import rooms_structure


class Rooms(Resource):
    method_decorators = [check_login]

    @marshal_with(rooms_structure)
    def get(self, room_number=None):
        if room_number:
            data = RoomsModel.query. \
                get_or_404(room_number, description='Room not found')
            return data
        return RoomsModel.query.all()

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

        if RoomsModel.query.get(number):
            return Response("This room is already exist", 412)

        if number > 0:
            if price > 0:
                if status in ['Free', 'Tenanted']:
                    new_room = RoomsModel(**data)
                    db.session.add(new_room)
                    db.session.commit()
                    return Response(f"Room was added {data}", 201)
                return Response("Status can be Free or Tenanted", 412)
            return Response("Price can't be negative", 412)
        return Response("Room number can't be negative", 412)

    def put(self, room_number):
        data = json.loads(request.data)
        room = RoomsModel.query.get(room_number)
        for key, value in data.items():
            setattr(room, key, value)
            room.status = "Attended" if key == "tenant_id" else "Available"
        db.session.commit()
        return f"Successfully updated the room number {room_number}"

    def delete(self, room_number):
        room = RoomsModel.query. \
            get_or_404(room_number, description='Room not found')
        db.session.delete(room)
        db.session.commit()
        return f"Successfully deleted the room number {room_number}"
