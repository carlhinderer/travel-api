import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config
from extensions import db


app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models



def create_app():
    env = os.environ.get('ENV', 'Development')

    if env == 'Production':
        config_str = 'config.ProductionConfig'
    elif env == 'Staging':
        config_str = 'config.StagingConfig'
    else:
        config_str = 'config.DevelopmentConfig'

    app = Flask(__name__)
    app.config.from_object(config_str)

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)





if __name__ == '__main__':
    app = create_app()
    app.run()