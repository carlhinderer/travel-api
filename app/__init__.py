import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    from .extensions import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import hotel
    app.register_blueprint(hotel.bp, url_prefix='/api/v1')

    return app
