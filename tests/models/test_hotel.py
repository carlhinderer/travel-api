import pytest

from app.models.hotel import Hotel


def test_can_save_hotel(app):
    with app.app_context():
        h = Hotel(name="Taj Mahal")
        h.save()
        assert Hotel.query.count() == 1
