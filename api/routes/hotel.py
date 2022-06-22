from flask import Blueprint, jsonify, request
from http import HTTPStatus

from models.hotel import Hotel
from schemas.hotel import HotelSchema


hotel = Blueprint(name='hotel', import_name=__name__)

hotel_schema = HotelSchema()
hotels_schema = HotelSchema(many=True)


@hotel.route('/hotels', methods=['GET'])
def hotel_list():
    all_hotels = Hotel.query.all()
    return jsonify(hotels_schema.dump(all_hotels))
