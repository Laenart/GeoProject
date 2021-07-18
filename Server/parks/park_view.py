from flask import Blueprint, jsonify, request
from flask_cors import cross_origin

from app import db, geo_model
from store.pois_getter import get_park_by_pois

parks_api = Blueprint('parks_api', __name__)


@parks_api.route('/parks', methods=['GET'])
@cross_origin(supports_credentials=True)
def all_parks():
    parks = geo_model.query.all()
    result = [
        {
            "Id": park.Id,
            "Latitude": park.Latitude,
            "Longitude": park.Longitude,
            "TypeId": park.TypeId,
            "Distance": park.Distance
        }
        for park in parks]
    return jsonify({
        'status': 'success',
        'parks': result
    })


@parks_api.route('/parks', methods=['PUT'])
@cross_origin(supports_credentials=True)
def add_parks():
    geo_model.query.delete()

    parks1 = get_park_by_pois()
    for park in parks1:
        db.session.add(park)

    db.session.commit()
    return jsonify({
        'status': 'success'
    })


@parks_api.route('/parks', methods=['DELETE'])
@cross_origin(supports_credentials=True)
def remove_park():
    park_id = request.json['park_id']
    park = geo_model.query.get(park_id)
    db.session.delete(park)
    db.session.commit()

    response_object = {'status': 'success'}
    return jsonify(response_object)

