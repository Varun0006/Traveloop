# Traveloop — Smart Travel Planning Platform

A full-stack web application for creating, organizing, and sharing travel itineraries with budget tracking, weather integration, and activity recommendations.

## 🎯 Features

- 📍 **Interactive Maps** - Visualize your trips on interactive maps
- 📅 **Smart Itineraries** - AI-powered day-by-day itinerary planning
- 💰 **Budget Tracking** - Track expenses and visualize spending
- ☁️ **Weather Integration** - Get forecasts for your destinations
- 🎒 **Packing Checklist** - Never forget anything again
- 🔗 **Easy Sharing** - Share your trips with friends
- 🌍 **Destination Discovery** - Find activities and attractions
- 💬 **Community Feed** - Share and discover travel inspiration

## 📋 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Installation

1. **Clone and setup**
```bash
git clone <repository-url>
cd Traveloop
```

2. **Python environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configuration**
```bash
cp .env.example .env
# Edit .env with your settings
```

4. **Database**
```bash
python scripts/init_db.py
```

5. **Frontend**
```bash
npm install
npm run dev  # Watch mode
```

6. **Run**
```bash
python main.py  # In another terminal
```

Access at: `http://localhost:5000`

For detailed setup instructions, see [docs/SETUP.md](docs/SETUP.md)

## 🏗️ Project Structure

```
Traveloop/
├── app/              # Flask application (models, routes, services, templates)
├── config/           # Configuration management
├── docs/             # Documentation
├── scripts/          # Utility scripts
├── tests/            # Test files
├── build/            # Build outputs
├── main.py           # Development entry point
├── wsgi.py           # Production entry point
└── ...
```

For detailed structure, see [docs/STRUCTURE.md](docs/STRUCTURE.md)

## 🚀 Development Phases

The project is organized into 10 development phases:

- **Phase 0**: Foundation Setup ✅
- **Phase 1**: Authentication (NEXT)
- **Phase 2**: Dashboard
- **Phases 3-10**: Features, optimization, deployment

See [plan.md](plan.md) for complete roadmap and timelines.

## 🔧 Available Commands

### Backend
```bash
python main.py              # Run development server
wsgi.py                    # Production entry point
python scripts/init_db.py  # Initialize database
flask db migrate           # Create migration
flask db upgrade           # Apply migrations
```

### Frontend
```bash
npm run dev                # Watch Tailwind CSS
npm run build              # Build Tailwind CSS
```

## 📁 Configuration

### `.env` File
```env
FLASK_ENV=development
FLASK_PORT=5000
SECRET_KEY=your-secret-key-here
SQLALCHEMY_DATABASE_URI=sqlite:///traveloop.db

# External APIs (add when needed)
GEODB_API_KEY=your-key
OPENTRIPMAP_API_KEY=your-key
OPENWEATHERMAP_API_KEY=your-key
OPENROUTESERVICE_API_KEY=your-key
UNSPLASH_API_KEY=your-key
```

See [.env.example](.env.example) for all available options.

## 🎨 Design System

### Colors
- **Primary**: Violet (#a855f7)
- **Background**: White/Gray-950
- **Text**: Gray-900/Gray-50

### Typography
- **Display**: Poppins
- **Body**: Inter

### Components
- Buttons (primary, secondary, outline, ghost)
- Cards (standard, glass effect)
- Forms (input, textarea, select)
- Badges
- Notifications

See [app/static/css/globals.css](app/static/css/globals.css) for component styles.

## 📚 Documentation

- [Setup Guide](docs/SETUP.md) - Detailed setup instructions
- [Project Structure](docs/STRUCTURE.md) - Directory organization
- [Development Plan](plan.md) - Phase roadmap and timeline
- [To-Do List](todo) - Current development tasks

## 🤝 Contributing

1. Create a feature branch (`git checkout -b feature/your-feature`)
2. Commit changes (`git commit -m 'Add your feature'`)
3. Push to branch (`git push origin feature/your-feature`)
4. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 📞 Support

For issues and questions, please open an issue on GitHub.

---

**Status**: Phase 0 Foundation Setup ✅ → Phase 1 Authentication (NEXT)  
**Last Updated**: May 10, 2026  
**Python**: 3.8+  
**Node**: 16+