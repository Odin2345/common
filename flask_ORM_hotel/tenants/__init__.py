from flask import Blueprint
from flask_restful import Api
from tenants.resource import Tenants, TenantRooms

tenants = Blueprint("tenants", __name__)
api_tenants = Api(tenants)

api_tenants.add_resource(Tenants,
                         "/tenants",
                         "/tenants/<string:passport>")
api_tenants.add_resource(TenantRooms,
                         "/tenant_rooms",
                         "/tenant_rooms/<string:passport>")
