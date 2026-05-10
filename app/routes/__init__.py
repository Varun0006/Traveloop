"""
Routes module for Traveloop

Phase 1 includes basic app structure.
Authentication routes will be added in Phase 2.
Trip management routes will be added in Phase 4.
"""

from flask import Blueprint, render_template
from flask_login import current_user

# Create blueprints for different route groups
main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
trips_bp = Blueprint('trips', __name__, url_prefix='/trips')


@main_bp.route('/')
def index():
    """Home page - Phase 1"""
    return render_template('pages/home.html')


@main_bp.route('/health')
def health():
    """Health check endpoint"""
    return {'status': 'ok', 'message': 'Traveloop API is running'}, 200


def register_blueprints(app):
    """Register all blueprints with the Flask app"""
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(trips_bp)
