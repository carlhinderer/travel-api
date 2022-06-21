import os

class BaseConfig:
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://travelapiuser:travelapipw@localhost/travelapi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-placeholder'


class TestConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'
