from flask import Blueprint, jsonify, request
from http import HTTPStatus

from app.models.hotel import Hotel
from app.schemas.hotel import HotelSchema


bp = Blueprint('hotel', __name__)

hotel_schema = HotelSchema()
hotels_schema = HotelSchema(many=True)


@bp.route('/hotels', methods=['GET'])
def hotel_list():
    all_hotels = Hotel.query.all()
    return jsonify(hotels_schema.dump(all_hotels))
