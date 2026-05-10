"""
Database initialization script

Usage:
    python scripts/init_db.py

This script initializes the database with tables for all models.
"""

import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db


def init_db():
    """Initialize database"""
    app = create_app()
    
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("✓ Database initialized successfully!")
        print(f"Database: {app.config.get('SQLALCHEMY_DATABASE_URI')}")


if __name__ == '__main__':
    init_db()
