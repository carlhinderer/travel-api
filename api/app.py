import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import config
from extensions import db

from routes.hotel import hotel


def create_app():
    app = Flask(__name__)
    add_config(app)
    register_extensions(app)
    register_blueprints(app)
    return app

def add_config(app):
    env = os.environ.get('APP_ENV', 'Development')

    if env == 'Production':
        config_str = 'config.ProductionConfig'
    elif env == 'Test':
        config_str = 'config.TestConfig'
    else:
        config_str = 'config.DevelopmentConfig'

    app.config.from_object(config_str)

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)

def register_blueprints(app):
    app.register_blueprint(hotel, url_prefix='/api/v1')


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
