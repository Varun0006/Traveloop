"""
Utilities module for Traveloop

Phase 1 includes basic utility functions.
Additional utilities will be added as needed in later phases.
"""

import os
from datetime import datetime


def get_env(key, default=None):
    """Get environment variable with optional default"""
    return os.getenv(key, default)


def log_action(action, details=None):
    """Log application actions"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {action}")
    if details:
        print(f"  Details: {details}")


# Additional utilities to be added:
# - Date formatting utilities
# - Currency conversion utilities
# - Distance calculation utilities
# - Map coordinate utilities
# - Error handling utilities
