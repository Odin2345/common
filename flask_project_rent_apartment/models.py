from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))


class ApartmentModel(db.Model):
    __tablename__ = 'apartments'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    city = db.Column(db.String(30))
    district = db.Column(db.String(30))
    rooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    owner = db.Column(db.String(30))
    representative = db.Column(db.String(30))


class BookingModel(db.Model):
    __tablename__ = 'booking'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    #apartment = db.relationship('ApartmentModel', backref='tenant')
    #contacts = db.Column(db.String, db.ForeignKey('users.email'))
    from_the_owner = db.Column(db.Boolean)
