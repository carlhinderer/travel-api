import pytest
import sqlalchemy as sa

from app import create_app, db


@pytest.fixture(scope="session")
def database():
    db_opts = sa.engine.url.make_url(DB_CONN).translate_connect_args()

@pytest.fixture(scope="session")
def app(database):
    app = create_app(TEST_CONFIG)

    with app.app_context():
        db.create_all()
        db.session.commit()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope="session")
def client(app):
    return app.test_client()

@pytest.fixture(scope="session")
def runner(app):
    return app.test_cli_runner()
