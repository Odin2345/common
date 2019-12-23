from db import db

staff_rooms = db.Table(
    'staff_rooms',
    db.Column('staff_passport',
              db.String,
              db.ForeignKey('staff.passport_id')),
    db.Column('room_number',
              db.Integer,
              db.ForeignKey('rooms.number'))
)


class RoomsModel(db.Model):
    __tablename__ = 'rooms'

    number = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    tenant_id = db.Column(db.String, db.ForeignKey('tenants.passport_id'))


class TenantsModel(db.Model):
    __tablename__ = 'tenants'

    passport_id = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(30), nullable=False)
    rooms = db.relationship('RoomsModel', backref='tenant')


class StaffModel(db.Model):
    __tablename__ = 'staff'

    passport_id = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    rooms = db.relationship('RoomsModel',
                            secondary=staff_rooms,
                            backref='rooms')


class UserModel(db.Model):
    __tablename__ = 'users'

    login = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String, nullable=False)
