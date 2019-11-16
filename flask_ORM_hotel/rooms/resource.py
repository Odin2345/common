import json
from flask import request
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
        new_room = RoomsModel(**data)
        db.session.add(new_room)
        db.session.commit()
        return f"Successfully added a new room {new_room.number}", 201

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
