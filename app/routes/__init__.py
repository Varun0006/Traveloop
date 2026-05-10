"""Core routes and blueprint registration for Traveloop."""

from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from app.routes.auth import auth_bp
from app.routes.dashboard import dashboard_bp
from app.routes.locations import locations_bp
from app.routes.itinerary_api import itinerary_bp
from app.routes.share_api import share_api_bp
from app.routes.community_api import community_api_bp
from app.routes.trip_api import trip_api_bp
from app.routes.admin_api import admin_api_bp

from app.routes.settings import settings_bp

# Create blueprints for different route groups
main_bp = Blueprint('main', __name__)
trips_bp = Blueprint('trips', __name__, url_prefix='/trips')

@main_bp.route('/')
def index():
    """Public home page."""
    return render_template('pages/home.html')

@main_bp.route('/profile')
@login_required
def profile_self():
    from app.models.trip import Trip
    public_trips = current_user.trips.filter_by(is_public=True).order_by(Trip.created_at.desc()).all()
    return render_template('pages/profile.html', user=current_user, public_trips=public_trips)

@main_bp.route('/profile/<username>')
def profile_view(username):
    from app.models.user import User
    from app.models.trip import Trip
    user = User.query.filter_by(username=username).first()
    if not user:
        return render_template('errors/404.html'), 404
    public_trips = user.trips.filter_by(is_public=True).order_by(Trip.created_at.desc()).all()
    return render_template('pages/profile.html', user=user, public_trips=public_trips)

@main_bp.route('/dashboard')
@login_required
def dashboard():
    """Protected dashboard page shown after login."""
    return render_template('pages/dashboard.html')

@main_bp.route('/community')
def community():
    """Community feed page."""
    return render_template('pages/community.html')

@main_bp.route('/share/<token>')
def public_trip(token):
    """Public read-only view of a trip."""
    from app.services.share_service import ShareService
    trip = ShareService.get_trip_by_token(token)
    if not trip:
        return render_template('errors/404.html'), 404
    return render_template('pages/shared_trip.html', trip=trip, token=token)

@main_bp.route('/admin')
def admin_dashboard():
    """Admin-only analytics dashboard."""
    if not current_user.is_authenticated:
        return redirect(url_for('auth.admin_login', next=request.path))

    if not current_user.is_admin:
        return render_template('errors/404.html'), 403
    return render_template('pages/admin.html')

@main_bp.route('/health')
def health():
    """Health check endpoint"""
    return {'status': 'ok', 'message': 'Traveloop API is running'}, 200

def register_blueprints(app):
    """Register all blueprints with the Flask app"""
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(trips_bp)
    app.register_blueprint(trip_api_bp)
    app.register_blueprint(locations_bp)
    app.register_blueprint(itinerary_bp)
    app.register_blueprint(share_api_bp)
    app.register_blueprint(community_api_bp)
    app.register_blueprint(admin_api_bp)
    app.register_blueprint(settings_bp)

@trips_bp.route('/')
@login_required
def my_trips():
    """Page displaying all user's trips"""
    return render_template('pages/my_trips.html')

@trips_bp.route('/<int:trip_id>')
@login_required
def trip_detail(trip_id):
    """Itinerary Builder page for a specific trip"""
    return render_template('pages/trip_detail.html', trip_id=trip_id)
