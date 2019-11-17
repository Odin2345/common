from datetime import timedelta
from flask import Flask

from search_apartment import search_apartment
from apartments import apartment
from config import run_config
from auth import auth
from create_db import create_db
from db import db
from users import user



def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)

    app.permanent_session_lifetime = timedelta(minutes=20)

    app.register_blueprint(auth)
    app.register_blueprint(create_db)
    app.register_blueprint(apartment)
    app.register_blueprint(search_apartment)
    app.register_blueprint(user)

    return app


if __name__ == '__main__':
    create_app().run()
