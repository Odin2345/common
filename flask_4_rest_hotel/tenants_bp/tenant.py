import json

from flask import Blueprint, Response, request
from flask_restful import Resource, marshal_with

from tenants_bp.resource import Tenants, TABLE, pars_tenant, tenants_structure
from rooms_bp.resource import TABLE as ROOM_TABLE

tenants_api_bp = Blueprint('GetTenants', __name__)


class GetTenants(Resource):
    @marshal_with(tenants_structure)
    def get(self):
        get_tenant = {
            "passport_id": [tenant for tenant in TABLE
                            if pars_tenant.parse_args().get('passport_id')
                            == tenant.passport_id],
            "room_number": [tenant for tenant in TABLE
                            if pars_tenant.parse_args().get('room_number')
                            == tenant.room_number]}

        for key, value in pars_tenant.parse_args().items():
            if value is not None:
                return get_tenant.get(key)
        else:
            return TABLE

    def post(self):
        data = json.loads(request.data)
        name = data.get('name')
        passport_id = data.get('passport_id')
        age = data.get('age')
        sex = data.get('sex')
        address = data.get('address')
        room_number = data.get('room_number')

        if None in [name, passport_id, age, sex, address, room_number]:
            return Response("You must fill in the staff information:"
                            " name, passport_id, age, sex, address,"
                            " room_number", 412)
        try:
            room_number = int(room_number)
            age = int(age)
        except ValueError:
            return Response("Age and room_number must be a number", 412)

        if str(passport_id) in [str(tenant.passport_id) for tenant in TABLE]:
            return Response("This tenant is already exist", 412)
        if age > 0:
            if str(room_number) in [str(room.number) for room in ROOM_TABLE]:
                new_tenant = Tenants(**data)
                TABLE.append(new_tenant)
                return Response(f"Tenant {passport_id} was added", 201)
            return Response("This room doesn't exist", 412)
        return Response("Age can't be negative", 412)

    def put(self, tenant_id):
        for tenant in TABLE:
            if tenant.passport_id == tenant_id:
                if pars_tenant.parse_args().get('room_number'):
                    tenant.room_number = pars_tenant.parse_args(). \
                        get('room_number')
                    return 'Information about tenant was updated', 200
        else:
            return 'Tenant not found', 404

    def delete(self, tenant_id):
        if tenant_id in [tenant.passport_id for tenant in TABLE]:
            [TABLE.remove(tenant) for tenant in TABLE
             if tenant.passport_id == tenant_id]
            return f"Tenant {tenant_id} was deleted"
        else:
            return Response("This tenant doesn't exist", 412)
