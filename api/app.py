import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from api.config import Config
from api.extensions import db

import api.models
from api.routes.hotel import hotel



def create_app():
    # env = os.environ.get('ENV', 'Development')

    # if env == 'Production':
        # config_str = 'config.ProductionConfig'
    # elif env == 'Staging':
        # config_str = 'config.StagingConfig'
    # else:
        # config_str = 'config.DevelopmentConfig'

    app = Flask(__name__)
    # app.config.from_object(config_str)
    app.config.from_object(Config)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)

def register_blueprints(app):
    app.register_blueprint(hotel, url_prefix='/api/v1')
