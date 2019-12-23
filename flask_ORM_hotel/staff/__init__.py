from flask import Blueprint
from flask_restful import Api
from staff.resource import Staff, StaffRoom

staff = Blueprint("staff", __name__)
api_staff = Api(staff)

api_staff.add_resource(Staff,
                       "/staff",
                       "/staff/<string:passport>")
api_staff.add_resource(StaffRoom,
                       "/staff_room",
                       "/staff_room/<string:passport>")
