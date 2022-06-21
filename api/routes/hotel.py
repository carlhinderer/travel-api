from flask import Blueprint, jsonify, request
from http import HTTPStatus

from models import Hotel

hotel = Blueprint(name='hotel', import_name=__name__)


@hotel.route('/hotels', methods=['GET'])
def get_hotels():
    hotel_name = Hotel.query.first().name
    return jsonify({'data': hotel_name})
