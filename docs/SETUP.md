# Setup Instructions

## Prerequisites

- Python 3.8+
- Node.js 16+
- Git

## Initial Setup

### 1. Clone and Navigate

```bash
git clone <repository-url>
cd Traveloop
```

### 2. Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Environment Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your settings
# Minimum requirements:
# - FLASK_ENV=development
# - SECRET_KEY=your-secret-key
# - SQLALCHEMY_DATABASE_URI=sqlite:///traveloop.db
```

### 4. Database Setup

```bash
# Initialize database
python scripts/init_db.py

# Or manually:
python
>>> from app import create_app, db
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

### 5. Frontend Setup

```bash
# Install Node dependencies
npm install

# Build Tailwind CSS
npm run build

# Or in watch mode for development:
npm run dev
```

## Running the Application

### Development Mode

**Terminal 1** - Watch Tailwind CSS:
```bash
npm run dev
```

**Terminal 2** - Run Flask server:
```bash
python main.py
```

Access the app at: `http://localhost:5000`

### Production Mode

```bash
# Build CSS once
npm run build

# Run with Gunicorn
gunicorn wsgi:app
```

## Database Migrations

```bash
# Create a new migration
flask db migrate -m "Description of changes"

# Apply migrations
flask db upgrade

# Downgrade one revision
flask db downgrade
```

## Troubleshooting

### Module not found errors
Make sure the virtual environment is activated:
```bash
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### Port already in use (5000)
Change the port in `.env`:
```env
FLASK_PORT=5001
```

### CSS not updating
1. Clear browser cache (Ctrl+Shift+Delete)
2. Rebuild Tailwind: `npm run build`
3. Restart Flask server

### Database errors
Reset the database:
```bash
rm traveloop.db  # Remove old database
python scripts/init_db.py  # Create new one
```

## Development Tips

1. **Auto-reload**: Flask development server auto-reloads on code changes
2. **Debug mode**: Set `FLASK_ENV=development` in `.env`
3. **Database browser**: Use `flask shell` to query the database
4. **Template testing**: Test templates with `{% debug %}` in templates

## Next Steps

1. Read the [project structure](STRUCTURE.md) to understand the codebase
2. Check the [phase guide](../../plan.md) for development roadmap
3. Start with Phase 1: Authentication
