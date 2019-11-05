from flask_restful import fields, reqparse


class Tenants(object):
    def __init__(self, name, passport_id, age, sex, address, room_number):
        self.name = name
        self.passport_id = passport_id
        self.age = age
        self.sex = sex
        self.address = address
        self.room_number = room_number


address_structure = {
    "city": fields.String,
    "street": fields.String
}

tenants_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "age": fields.Integer,
    "sex": fields.String,
    "address": fields.Nested(address_structure),
    "room_number": fields.Integer
}

pars_tenant = reqparse.RequestParser(bundle_errors=True)
pars_tenant.add_argument('name', type=str, help='Name is incorrect')
pars_tenant.add_argument('passport_id', type=str, help='Passport is incorrect')
pars_tenant.add_argument('age', type=int, help='Age must be int')
pars_tenant.add_argument('sex', type=str, help='Sex is incorrect')
pars_tenant.add_argument('address', type=dict, help='Address is incorrect')
pars_tenant.add_argument('room_number', type=int,
                         help='Number of room must be int')

TABLE = [Tenants('Mariya', 'OP876253', 24, 'female',
                 {"city": "Kiev", "street": "Zoloti Vorota"}, 8),
         Tenants('Ann', 'AI534621', 32, 'female',
                 {"city": "Dnipro", "street": "Topolinaya"}, 9),
         Tenants('Kyrylo', 'AE535679', 20, 'male',
                 {"city": "Lviv", "street": "Geroiv"}, 2),
         Tenants('Kate', 'IO534724', 45, 'female',
                 {"city": "Kiev", "street": "Gogolia"}, 2),
         Tenants('Roman', 'OO817678', 51, 'male',
                 {"city": "Lviv", "street": "Svobody"}, 6),
         Tenants('Serhii', 'PO987901', 20, 'male',
                 {"city": "Kiev", "street": "Pushkina"}, 9),
         Tenants('Pavel', 'IH768342', 35, 'male',
                 {"city": "Donetsk", "street": "Savchenko"}, 2),
         Tenants('Dmitriy', 'HH612563', 28, 'male',
                 {"city": "Kharkiv", "street": "Svobody"}, 6),
         Tenants('Taras', 'IT783567', 31, 'male',
                 {"city": "Dnipro", "street": "Krasnaya"}, 8),
         Tenants('Valentin', 'BA627901', 36, 'male',
                 {"city": "Pavlograd", "street": "Kirova"}, 3)]
