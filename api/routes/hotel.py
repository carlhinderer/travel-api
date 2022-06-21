from flask import Blueprint, jsonify, request
from http import HTTPStatus

# from models import Hotel

hotel = Blueprint(name='hotel', import_name=__name__)


@hotel.route('/hotels', methods=['GET'])
def get_hotels():
    return jsonify({'data': 'Data Here!'})
