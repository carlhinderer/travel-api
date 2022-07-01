import pytest
import sqlalchemy as sa

from app import create_app
from app.extensions import db


# @pytest.fixture(scope="session")
# def database():
    # db.create_all()
    # db.session.commit()
    # yield

@pytest.fixture(scope="session")
def app():
    app = create_app()

    with app.app_context():
        db.create_all()
        # db.session.commit()
        yield app
        # db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
