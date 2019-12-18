from flask_restful import fields, reqparse


class Staff(object):
    def __init__(self, name, passport_id, position, salary):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary


staff_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "position": fields.String,
    "salary": fields.Integer}

pars_staff = reqparse.RequestParser(bundle_errors=True)
pars_staff.add_argument('name', type=str, help='Name is incorrect')
pars_staff.add_argument('passport_id', type=str, help='Passport is incorrect')
pars_staff.add_argument('position', type=str, help='Position is incorrect')
pars_staff.add_argument('salary', type=int, help='Salary must be int')

TABLE = [Staff('Oleg', 'AK987253', 'Hostess', 12300),
         Staff('Ann', 'TA224356', 'Cook', 13500),
         Staff('Alex', 'OI768905', 'Waiter', 12400),
         Staff('Michael', 'AC656789', 'Housekeeper', 6700),
         Staff('Anastasiia', 'AE768789', 'Administrator', 14500),
         Staff('Greg', 'AO890095', 'Waiter', 12400),
         Staff('Vladimir', 'AC123213', 'Housekeeper', 6700),
         Staff('Ann', 'OO768954', 'Hostess', 12300),
         Staff('Kate', 'II788741', 'Cook', 7500),
         Staff('Victory', 'PO635267', 'Cook', 10000)]
