import json
from flask import request, Response
from flask_restful import Resource, marshal_with

from db import db
from models import TenantsModel, RoomsModel
from utils import check_login
from rooms.marshal_structure import rooms_structure
from tenants.marshal_structure import tenants_structure


class Tenants(Resource):
    method_decorators = [check_login]

    @marshal_with(tenants_structure)
    def get(self, passport=None):
        if passport:
            data = TenantsModel.query. \
                get_or_404(passport, description='Tenant not found')
            return data
        return TenantsModel.query.all()

    def post(self):
        data = json.loads(request.data)
        name = data.get('name')
        passport_id = data.get('passport_id')
        age = data.get('age')
        sex = data.get('sex')
        city = data.get('city')
        address = data.get('address')

        if None in [name, passport_id, age, sex, city, address]:
            return Response("You must fill in the staff information:"
                            " name, passport_id, age, sex, city, address",
                            412)
        try:
            age = int(age)
        except ValueError:
            return Response("Age must be a number", 412)

        if TenantsModel.query.get(passport_id):
            return Response("This tenant is already exist", 412)

        if len(passport_id) != 8:
            return Response("Passport must contain 8 characters", 412)

        if age > 0:
            if sex in ['male', 'female']:
                new_tenant = TenantsModel(**data)
                db.session.add(new_tenant)
                db.session.commit()
                return Response(f"Tenant {name} was added {data}", 201)
            return Response("Sex can be male or female", 412)
        return Response("Age can't be negative", 412)

    def put(self, passport):
        data = json.loads(request.data)
        tenant = TenantsModel.query.get(passport)
        for key, value in data.items():
            setattr(tenant, key, value)
        db.session.commit()
        return f"Successfully updated the tenant {tenant.name} ({passport})"

    def delete(self, passport):
        tenant = TenantsModel.query. \
            get_or_404(passport, description='Tenant not found')
        db.session.delete(tenant)
        db.session.commit()
        return f"Successfully deleted the tenant {tenant.name} ({passport})"


class TenantRooms(Resource):
    method_decorators = [check_login]

    @marshal_with(rooms_structure)
    def get(self, passport):
        tenant = TenantsModel.query. \
            get_or_404(passport, description='Tenant not found')
        return tenant.rooms

    def post(self):
        data = json.loads(request.data)
        tenant_passport = data.get("tenant_passport")
        room_number = data.get("room_number")

        tenant = TenantsModel.query. \
            get_or_404(tenant_passport, description='Tenant not found')
        room = RoomsModel.query. \
            get_or_404(room_number, description='Room not found')

        if not room.tenant_id:
            tenant.rooms.append(room)
            db.session.commit()
            return f"Successfully added room {room.number} " \
                f"to {tenant.name} ({tenant.passport_id})"
        else:
            return f"Room {room.number} tenanted"
