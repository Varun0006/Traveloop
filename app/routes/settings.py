from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.models.user import User

settings_bp = Blueprint('settings', __name__, url_prefix='/settings')

@settings_bp.route('/', methods=['GET'])
@login_required
def settings_page():
    return render_template('pages/settings.html')

@settings_bp.route('/api/profile', methods=['POST'])
@login_required
def update_profile():
    import os
    from werkzeug.utils import secure_filename
    from flask import current_app

    # Use request.form for multipart/form-data
    username = request.form.get('username')
    profile_picture_url = request.form.get('profile_picture')
    
    if username and username.strip():
        username = username.strip()
        existing = User.query.filter_by(username=username).first()
        if existing and existing.id != current_user.id:
            return jsonify({'error': 'Username already taken'}), 400
        current_user.username = username
        
    if profile_picture_url:
        current_user.profile_picture = profile_picture_url.strip()
        
    # Handle file upload if present
    if 'profile_image' in request.files:
        file = request.files['profile_image']
        if file and file.filename:
            filename = secure_filename(f"user_{current_user.id}_{file.filename}")
            upload_dir = os.path.join(current_app.root_path, 'static', 'uploads')
            os.makedirs(upload_dir, exist_ok=True)
            file_path = os.path.join(upload_dir, filename)
            file.save(file_path)
            current_user.profile_picture = f"/static/uploads/{filename}"
        
    db.session.commit()
    return jsonify({
        'success': True, 
        'message': 'Profile updated successfully',
        'username': current_user.username,
        'profile_picture': current_user.profile_picture
    }), 200
