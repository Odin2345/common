import json
from flask import request
from flask_restful import Resource, marshal_with

from db import db
from models import StaffModel, RoomsModel
from utils import check_login
from staff.marshal_structure import staff_structure
from rooms.marshal_structure import rooms_structure


class Staff(Resource):
    method_decorators = [check_login]

    @marshal_with(staff_structure)
    def get(self, passport=None):
        if passport:
            data = StaffModel.query.get_or_404(passport,
                                               description='Worker not found')
            return data
        return StaffModel.query.all()

    def post(self):
        data = json.loads(request.data)
        new_worker = StaffModel(**data)
        db.session.add(new_worker)
        db.session.commit()
        return f"Successfully added a new worker " \
                   f"{new_worker.name} ({new_worker.passport_id})", 201

    def put(self, passport):
        data = json.loads(request.data)
        worker = StaffModel.query.get(passport)
        for key, value in data.items():
            setattr(worker, key, value)
            db.session.commit()
        return f"Successfully updated the worker {worker.name} ({passport})"

    def delete(self, passport):
        worker = StaffModel.query.get_or_404(passport,
                                             description='Worker not found')
        db.session.delete(worker)
        db.session.commit()
        return f"Successfully deleted the worker {worker.name} ({passport})"


class StaffRoom(Resource):
    method_decorators = [check_login]

    def post(self):
        data = json.loads(request.data)
        staff_passport = data.get("staff_passport")
        room_number = data.get("room_number")
        worker = StaffModel.query. \
            filter_by(passport_id=staff_passport). \
            first_or_404(description='Worker not found')
        room = RoomsModel.query. \
            filter_by(number=room_number). \
            first_or_404(description='Room not found')
        worker.rooms.append(room)
        db.session.commit()
        return f"Successfully added room {room.number} " \
            f"to {worker.name} ({worker.passport_id})"

    @marshal_with(rooms_structure)
    def get(self, passport):
        worker = StaffModel.query. \
            get_or_404(passport, description='Worker not found')
        return worker.rooms
