from flask_restful import fields

rooms_structure = {
    'number': fields.Integer,
    'level': fields.Integer,
    'status': fields.String,
    'price': fields.Integer,
    'tenant_id': fields.String
}
