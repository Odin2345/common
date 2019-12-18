import json

from flask import Blueprint, Response, request
from flask_restful import Resource, marshal_with

from staff_bp.resource import Staff, TABLE, pars_staff, staff_structure

staff_api_bp = Blueprint('GetStaff', __name__)


class GetStaff(Resource):
    @marshal_with(staff_structure)
    def get(self):
        passport_id = pars_staff.parse_args().get('passport_id')
        position = pars_staff.parse_args().get('position')
        get_staff = {
            "passport_id": [staff for staff in TABLE
                            if passport_id == staff.passport_id],
            "position": [staff for staff in TABLE
                         if position == staff.position]}

        for key, value in pars_staff.parse_args().items():
            if value is not None:
                return get_staff.get(key)
        else:
            return TABLE

    def post(self):
        data = json.loads(request.data)
        name = data.get('name')
        passport_id = data.get('passport_id')
        position = data.get('position')
        salary = data.get('salary')

        if None in [name, passport_id, position, salary]:
            return Response("You must fill in the staff information:"
                            " name, passport_id, position, salary", 412)
        try:
            salary = int(salary)
        except ValueError:
            return Response("Salary must be a number", 412)

        if str(passport_id) in [str(staff.passport_id) for staff in TABLE]:
            return Response("This staff is already exist", 412)
        if salary > 0:
            new_staff = Staff(**data)
            TABLE.append(new_staff)
            return Response(f"Staff {passport_id} was added", 201)
        return Response("Salary can't be negative", 412)

    def put(self, staff_id):
        for staff in TABLE:
            if staff.passport_id == staff_id:
                if pars_staff.parse_args().get('name'):
                    staff.name = pars_staff.parse_args().get('name')
                if pars_staff.parse_args().get('position'):
                    staff.position = pars_staff.parse_args().get('position')
                if pars_staff.parse_args().get('salary'):
                    staff.salary = pars_staff.parse_args().get('salary')
                return 'Information about staff was updated', 200
        else:
            return 'Staff not found', 404

    def delete(self, staff_id):
        if staff_id in [staff.passport_id for staff in TABLE]:
            [TABLE.remove(staff) for staff in TABLE
             if staff.passport_id == staff_id]
            return f"Staff {staff_id} was deleted"
        else:
            return Response("This staff doesn't exist", 412)
