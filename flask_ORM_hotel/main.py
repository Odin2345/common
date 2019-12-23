from datetime import timedelta
from flask import Flask

from config import run_config
from auth import auth
from create_db import create_db
from db import db
from rooms import rooms
from staff import staff
from tenants import tenants


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)
    app.permanent_session_lifetime = timedelta(minutes=20)

    app.register_blueprint(auth)
    app.register_blueprint(rooms)
    app.register_blueprint(staff)
    app.register_blueprint(tenants)
    app.register_blueprint(create_db)

    return app


if __name__ == '__main__':
    create_app().run()
