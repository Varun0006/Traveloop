"""
Routes module for Traveloop

Phase 1 includes basic app structure.
Authentication routes will be added in Phase 2.
Trip management routes will be added in Phase 4.
"""

from flask import Blueprint

# Create blueprints for different route groups
main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
trips_bp = Blueprint('trips', __name__, url_prefix='/trips')


@main_bp.route('/')
def index():
    """Home page - Phase 1 placeholder"""
    return {'message': 'Welcome to Traveloop!'}, 200


@main_bp.route('/health')
def health():
    """Health check endpoint"""
    return {'status': 'healthy'}, 200


def register_blueprints(app):
    """Register all blueprints with the app"""
    app.register_blueprint(main_bp)
    # auth_bp will be registered in Phase 2
    # trips_bp will be registered in Phase 4
