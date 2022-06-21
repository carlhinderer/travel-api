import os

class Config(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-placeholder'

    SQLALCHEMY_DATABASE_URI = 'postgresql://travelapiuser:travelapipw@localhost/travelapi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
