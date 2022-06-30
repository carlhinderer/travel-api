import os

FLASK_ENV = 'development'
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgresql://travelapiuser:travelapipw@localhost/travelapi'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-placeholder'


# Test Config
# TESTING = True
# SQLALCHEMY_DATABASE_URI = 'postgresql://travelapitestuser:travelapitestpw@localhost/travelapitest'
# SQLALCHEMY_TRACK_MODIFICATIONS = False
