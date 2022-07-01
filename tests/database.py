import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy

from config import settings


# Need this for pytest-flask-sqlalchemy extension
db = SQLAlchemy()
engine = sa.create_engine(settings['TEST']['SQLALCHEMY_DATABASE_URI'])
