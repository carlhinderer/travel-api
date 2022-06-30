import os

from flask import Flask
from dynaconf import FlaskDynaconf


def create_app():
    app = Flask(__name__)
    FlaskDynaconf(app)

    from .extensions import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import hotel
    app.register_blueprint(hotel.bp, url_prefix='/api/v1')

    return app
