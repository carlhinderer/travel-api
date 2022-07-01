import pytest
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from app.extensions import db


@pytest.fixture(scope="session")
def app():
    app = create_app()

    with app.app_context():
        db.create_all()
        db.session.commit()
        yield app
        db.session.remove()
        db.drop_all()

# Need this for pytest-flask-sqlalchemy extension
@pytest.fixture(scope="session")
def _db(app):
    database = SQLAlchemy(app=app)
    return database

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
