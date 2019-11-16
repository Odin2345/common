from flask import Blueprint
from flask_restful import Api
from rooms.resource import Rooms

rooms = Blueprint("rooms", __name__)
api_rooms = Api(rooms)

api_rooms.add_resource(Rooms, "/rooms", "/rooms/<int:room_number>")
