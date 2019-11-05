from flask import Blueprint
from flask_restful import Resource, marshal_with

from staff_bp.resource import Staff, TABLE, pars_staff, staff_structure

staff_api_bp = Blueprint('GetStaff', __name__)


class GetStaff(Resource):
    @marshal_with(staff_structure)
    def get(self):
        get_staff = {
            "passport_id": [staff for staff in TABLE
                            if pars_staff.parse_args().get('passport_id')
                            == staff.passport_id],
            "position": [staff for staff in TABLE
                         if pars_staff.parse_args().get('position')
                         == staff.position]}

        for key, value in pars_staff.parse_args().items():
            if value is not None:
                return get_staff.get(key)
        else:
            return TABLE

    def post(self):
        staff_id = pars_staff.parse_args().get('passport_id')
        for staff in TABLE:
            if staff.passport_id == staff_id:
                return f'Staff {staff.name} {staff.passport_id}' \
                    f' already added to system'
        TABLE.append(Staff(pars_staff.parse_args().get('name'),
                           staff_id,
                           pars_staff.parse_args().get('position'),
                           pars_staff.parse_args().get('salary')))
        return f'Staff added to system ({staff_id})', 201

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

    @marshal_with(staff_structure)
    def delete(self, staff_id):
        for staff in TABLE:
            if staff.passport_id == staff_id:
                TABLE.remove(staff)
        return TABLE, 200
