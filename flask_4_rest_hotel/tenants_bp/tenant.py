from flask import Blueprint
from flask_restful import Resource, marshal_with

from tenants_bp.resource import Tenants, TABLE, pars_tenant, tenants_structure

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
        tenant_id = pars_tenant.parse_args().get('passport_id')
        for tenant in TABLE:
            if tenant.passport_id == tenant_id:
                return f'Tenant {tenant.name} {tenant.passport_id} ' \
                    f'already added to system'
        TABLE.append(Tenants(pars_tenant.parse_args().get('name'),
                             tenant_id,
                             pars_tenant.parse_args().get('age'),
                             pars_tenant.parse_args().get('sex'),
                             {"city": pars_tenant.parse_args().
                             get('address').get('city'),
                              "street": pars_tenant.parse_args().
                             get('address').get('street')},
                             pars_tenant.parse_args().get('room_number')))
        return f'Tenant added to system ({tenant_id})', 201

    def put(self, tenant_id):
        for tenant in TABLE:
            if tenant.passport_id == tenant_id:
                if pars_tenant.parse_args().get('room_number'):
                    tenant.room_number = pars_tenant.parse_args().\
                        get('room_number')
                    return 'Information about tenant was updated', 200
        else:
            return 'Tenant not found', 404

    @marshal_with(tenants_structure)
    def delete(self, tenant_id):
        for tenant in TABLE:
            if tenant.passport_id == tenant_id:
                TABLE.remove(tenant)
        return TABLE, 200
