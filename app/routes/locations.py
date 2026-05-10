"""
Locations API routes - Phase 4
"""

from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.services.location_service import LocationService

locations_bp = Blueprint('locations', __name__, url_prefix='/api/locations')

@locations_bp.route('/cities/autocomplete', methods=['GET'])
def autocomplete_cities():
    from flask_login import current_user
    if not current_user.is_authenticated:
        return jsonify({'error': 'Unauthorized'}), 401
    query = request.args.get('q', '')
    if len(query) < 2:
        return jsonify([]), 200
    
    cities = LocationService.search_cities(query)
    return jsonify(cities), 200

@locations_bp.route('/attractions', methods=['GET'])
def get_attractions():
    from flask_login import current_user
    if not current_user.is_authenticated:
        return jsonify({'error': 'Unauthorized'}), 401
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)
    
    if lat is None or lon is None:
        return jsonify({'error': 'Latitude and longitude are required'}), 400
    
    attractions = LocationService.get_attractions(lat, lon)
    return jsonify(attractions), 200

@locations_bp.route('/city-image', methods=['GET'])
def get_city_image():
    from flask_login import current_user
    if not current_user.is_authenticated:
        return jsonify({'error': 'Unauthorized'}), 401
    city = request.args.get('city', '')
    if not city:
        return jsonify({'error': 'City name is required'}), 400
    
    image_url = LocationService.get_city_image(city)
    return jsonify({'url': image_url}), 200
