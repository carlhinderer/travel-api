import pytest

from app.models.hotel import Hotel


@pytest.fixture
def saved_hotel(app):
    h = Hotel(name='Grand Budapest Hotel',
              continent_name='Europe',
              city_name='Budapest',
              country_name='Hungary')
    h.save()
    yield
    h.delete()


def test_use_fixture(saved_hotel):
    assert Hotel.query.count() == 1

def test_dont_use_fixture():
    assert Hotel.query.count() == 0

def test_can_save_hotel(db_session):
    h = Hotel(name="Stanley Hotel")
    db_session.add(h)
    db_session.commit()
    assert db_session.query(Hotel).count() == 1

def test_clean_between_tests():
    assert Hotel.query.count() == 0
