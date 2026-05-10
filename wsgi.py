"""
WSGI Entry Point

Use this file for production deployments with Gunicorn, uWSGI, or other WSGI servers:
    gunicorn wsgi:app
    uwsgi --http :5000 --wsgi-file wsgi.py --callable app
"""

import os
from app import create_app

app = create_app(os.getenv('FLASK_ENV', 'production'))

if __name__ == '__main__':
    app.run()
