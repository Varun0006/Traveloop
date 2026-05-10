# Traveloop Project Structure

## Directory Layout

```
Traveloop/
├── app/                          # Main Flask application
│   ├── __init__.py              # Flask app factory
│   ├── models/                  # Database models
│   │   ├── __init__.py
│   │   └── user.py              # User model (Phase 1+)
│   ├── routes/                  # API endpoints (blueprints)
│   │   ├── __init__.py
│   │   ├── auth.py              # Auth routes (Phase 1)
│   │   ├── dashboard.py         # Dashboard (Phase 2)
│   │   ├── trips.py             # Trip CRUD (Phase 3)
│   │   ├── activities.py        # Activities (Phase 3)
│   │   ├── locations.py         # Locations/Search (Phase 4)
│   │   ├── itinerary.py         # Itinerary (Phase 5)
│   │   ├── budget.py            # Budget (Phase 6)
│   │   ├── packing.py           # Packing (Phase 6)
│   │   ├── notes.py             # Notes (Phase 6)
│   │   ├── sharing.py           # Sharing (Phase 7)
│   │   ├── community.py         # Community (Phase 7)
│   │   └── admin.py             # Admin (Phase 8)
│   ├── services/                # Business logic
│   │   ├── __init__.py
│   │   ├── user_service.py      # User operations
│   │   ├── trip_service.py      # Trip operations
│   │   ├── location_service.py  # Location APIs
│   │   ├── weather_service.py   # Weather APIs
│   │   ├── route_service.py     # Route APIs
│   │   ├── image_service.py     # Image APIs
│   │   ├── itinerary_service.py # Itinerary logic
│   │   ├── budget_service.py    # Budget logic
│   │   ├── sharing_service.py   # Sharing logic
│   │   └── analytics_service.py # Analytics
│   ├── utils/                   # Utilities
│   │   ├── __init__.py
│   │   ├── decorators.py        # Custom decorators
│   │   ├── validators.py        # Data validation
│   │   ├── response.py          # API responses
│   │   ├── errors.py            # Custom errors
│   │   ├── constants.py         # Constants
│   │   ├── cache.py             # Caching
│   │   └── helpers.py           # Helper functions
│   ├── static/                  # Static assets (compiled & source)
│   │   ├── css/
│   │   │   ├── globals.css      # Global styles
│   │   │   └── output.css       # Compiled TailwindCSS
│   │   ├── js/
│   │   │   ├── app.js           # App utilities
│   │   │   └── theme.js         # Dark mode
│   │   └── images/              # Static images
│   └── templates/               # Jinja2 templates
│       ├── base.html            # Master template
│       ├── components/
│       │   ├── navbar.html
│       │   └── footer.html
│       └── pages/
│           ├── home.html
│           ├── auth/            # Auth pages (Phase 1)
│           ├── dashboard/       # Dashboard (Phase 2)
│           ├── trips/           # Trip pages (Phase 3)
│           └── ...              # More pages as added
│
├── config/                      # Configuration
│   └── __init__.py             # All configs (development, production, testing)
│
├── build/                       # Build outputs
│   ├── css/                    # Compiled CSS (Git ignored)
│   └── js/                     # Compiled JS (Git ignored)
│
├── docs/                        # Documentation
│   ├── STRUCTURE.md            # This file
│   ├── SETUP.md                # Setup instructions
│   ├── PHASE_GUIDE.md          # Phase development guide
│   └── API.md                  # API documentation (future)
│
├── migrations/                 # Database migrations (Flask-Migrate)
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│
├── scripts/                    # Utility scripts
│   ├── __init__.py
│   ├── init_db.py             # Database initialization
│   └── seed_data.py           # Sample data (future)
│
├── tests/                      # Test files
│   ├── __init__.py
│   ├── test_models.py         # Model tests
│   ├── test_routes.py         # Route tests
│   └── test_services.py       # Service tests
│
├── .env                        # Environment variables (Git ignored)
├── .env.example               # Environment template
├── .gitignore                 # Git ignore patterns
├── .python-version            # Python version (pyenv)
├── LICENSE                    # MIT License
├── README.md                  # Main documentation
├── main.py                    # Development entry point
├── wsgi.py                    # Production entry point
├── package.json               # Node.js dependencies
├── postcss.config.js          # PostCSS config
├── pyproject.toml             # Python project metadata
├── requirements.txt           # Python dependencies
├── tailwind.config.js         # Tailwind CSS config
├── todo                       # Development todo list
└── uv.lock                    # UV lockfile
```

## Key Directories

### `/app`
Main Flask application containing all backend logic and frontend templates. Organized by function (models, routes, services, utils).

### `/config`
Configuration management for different environments (development, production, testing).

### `/docs`
Documentation files including setup guides, phase progress, and API documentation.

### `/scripts`
Utility scripts for database initialization, seeding, and other maintenance tasks.

### `/tests`
Automated tests for models, routes, and services.

### `/build`
Build outputs from Tailwind CSS compilation (should be in .gitignore).

### Root Level Files
- **main.py**: Run this for development (`python main.py`)
- **wsgi.py**: Use this for production deployments (`gunicorn wsgi:app`)
- **.env.example**: Template for environment variables
- **requirements.txt**: Python package dependencies
- **package.json**: Node.js packages (Tailwind, Flowbite, etc.)

## Development Workflow

1. **Setup**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   npm install
   ```

2. **Database**:
   ```bash
   flask db upgrade  # Run migrations
   python scripts/init_db.py  # Initialize database
   ```

3. **Development**:
   ```bash
   npm run dev  # Watch Tailwind CSS (in another terminal)
   python main.py  # Start Flask app
   ```

4. **Production**:
   ```bash
   gunicorn wsgi:app
   ```

## Adding New Features

1. Create models in `/app/models/`
2. Create services in `/app/services/`
3. Create routes in `/app/routes/`
4. Create templates in `/app/templates/`
5. Add tests in `/tests/`

Keep the structure organized and follow this pattern for consistency.
