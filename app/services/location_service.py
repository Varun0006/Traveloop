"""
Location Service for Phase 4
Handles interactions with GeoDB Cities, OpenTripMap, and Unsplash APIs.
"""

import os
import requests
import logging

logger = logging.getLogger(__name__)

class LocationService:
    _cache = {}

    @staticmethod
    def _get_api_keys():
        return {
            'geodb': os.getenv('GEODB_API_KEY'),
            'opentripmap': os.getenv('OPENTRIPMAP_API_KEY'),
            'unsplash': os.getenv('UNSPLASH_API_KEY')
        }

    @staticmethod
    def search_cities(query):
        """Search for cities using GeoDB Cities API"""
        query = query.strip().lower()
        if query in LocationService._cache:
            return LocationService._cache[query]

        keys = LocationService._get_api_keys()
        api_key = keys['geodb']
        
        if not api_key or api_key == 'your-geodb-api-key':
            logger.warning("GeoDB API Key missing, using mock data")
            return LocationService._mock_city_search(query)

        url = "https://geodb-cities-api.p.rapidapi.com/v1/geo/cities"
        querystring = {"namePrefix": query, "limit": "5", "sort": "-population"}
        headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "geodb-cities-api.p.rapidapi.com"
        }

        try:
            response = requests.get(url, headers=headers, params=querystring, timeout=10)
            response.raise_for_status()
            data = response.json()
            results = [
                {
                    'id': city['id'],
                    'name': city['city'],
                    'region': city['region'],
                    'country': city['country'],
                    'latitude': city['latitude'],
                    'longitude': city['longitude']
                } for city in data.get('data', [])
            ]
            LocationService._cache[query] = results
            return results
        except Exception as e:
            logger.error(f"GeoDB Search Error: {e}")
            return LocationService._mock_city_search(query)

    @staticmethod
    def get_attractions(lat, lon, radius=5000):
        """Get tourist attractions using OpenTripMap API"""
        keys = LocationService._get_api_keys()
        api_key = keys['opentripmap']

        if not api_key or api_key == 'your-opentripmap-api-key':
            logger.warning("OpenTripMap API Key missing, using mock data")
            return LocationService._mock_attractions(lat, lon)

        url = f"https://api.opentripmap.com/0.1/en/places/radius"
        params = {
            "radius": radius,
            "lon": lon,
            "lat": lat,
            "format": "json",
            "apikey": api_key,
            "kinds": "interesting_places,tourist_facilities"
        }

        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            # Filter and limit to 10 attractions
            return [
                {
                    'xid': place['xid'],
                    'name': place.get('name', 'Unnamed Place'),
                    'kinds': place.get('kinds', ''),
                    'latitude': place['point']['lat'],
                    'longitude': place['point']['lon'],
                    'dist': place.get('dist', 0)
                } for place in data if place.get('name')
            ][:10]
        except Exception as e:
            logger.error(f"OpenTripMap Error: {e}")
            return LocationService._mock_attractions(lat, lon)

    @staticmethod
    def get_city_image(city_name):
        """Fetch a city image from Unsplash"""
        keys = LocationService._get_api_keys()
        api_key = keys['unsplash']

        if not api_key or api_key == 'your-unsplash-api-key':
            return "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&q=80&w=1000"

        url = "https://api.unsplash.com/search/photos"
        params = {
            "query": f"{city_name} skyline",
            "per_page": 1,
            "client_id": api_key
        }

        try:
            response = requests.get(url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            if data['results']:
                return data['results'][0]['urls']['regular']
        except Exception as e:
            logger.error(f"Unsplash Error: {e}")
        
        return "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&q=80&w=1000"

    # --- Mock Helpers ---
    @staticmethod
    def _mock_city_search(query):
        mocks = [
            {'id': 1, 'name': 'Paris', 'region': 'Île-de-France', 'country': 'France', 'latitude': 48.8566, 'longitude': 2.3522},
            {'id': 2, 'name': 'New York', 'region': 'New York', 'country': 'United States', 'latitude': 40.7128, 'longitude': -74.0060},
            {'id': 3, 'name': 'Tokyo', 'region': 'Tokyo', 'country': 'Japan', 'latitude': 35.6895, 'longitude': 139.6917},
            {'id': 4, 'name': 'London', 'region': 'England', 'country': 'United Kingdom', 'latitude': 51.5074, 'longitude': -0.1278},
            {'id': 5, 'name': 'Berlin', 'region': 'Berlin', 'country': 'Germany', 'latitude': 52.5200, 'longitude': 13.4050},
            {'id': 6, 'name': 'Hyderabad', 'region': 'Telangana', 'country': 'India', 'latitude': 17.3850, 'longitude': 78.4867},
            {'id': 7, 'name': 'Mumbai', 'region': 'Maharashtra', 'country': 'India', 'latitude': 19.0760, 'longitude': 72.8777},
            {'id': 8, 'name': 'Bangalore', 'region': 'Karnataka', 'country': 'India', 'latitude': 12.9716, 'longitude': 77.5946},
            {'id': 9, 'name': 'Chennai', 'region': 'Tamil Nadu', 'country': 'India', 'latitude': 13.0827, 'longitude': 80.2707},
            {'id': 10, 'name': 'Delhi', 'region': 'Delhi', 'country': 'India', 'latitude': 28.6139, 'longitude': 77.2090},
            {'id': 11, 'name': 'Vadodara', 'region': 'Gujarat', 'country': 'India', 'latitude': 22.3072, 'longitude': 73.1812},
            {'id': 12, 'name': 'Ahmedabad', 'region': 'Gujarat', 'country': 'India', 'latitude': 23.0225, 'longitude': 72.5714},
        ]
        return [c for c in mocks if query.lower() in c['name'].lower()]

    @staticmethod
    def _mock_attractions(lat, lon):
        # Hyderabad specific mocks
        if 17.3 <= lat <= 17.5 and 78.4 <= lon <= 78.6:
            return [
                {'xid': 'h1', 'name': 'Charminar', 'kinds': 'historic', 'latitude': 17.3616, 'longitude': 78.4747},
                {'xid': 'h2', 'name': 'Golconda Fort', 'kinds': 'forts', 'latitude': 17.3833, 'longitude': 78.4011},
                {'xid': 'h3', 'name': 'Salar Jung Museum', 'kinds': 'museums', 'latitude': 17.3713, 'longitude': 78.4804},
                {'xid': 'h4', 'name': 'Hussain Sagar', 'kinds': 'lakes', 'latitude': 17.4239, 'longitude': 78.4738},
            ]
        
        # Delhi specific mocks
        if 28.5 <= lat <= 28.7 and 77.1 <= lon <= 77.3:
            return [
                {'xid': 'd1', 'name': 'Red Fort', 'kinds': 'historic', 'latitude': 28.6562, 'longitude': 77.2410},
                {'xid': 'd2', 'name': 'India Gate', 'kinds': 'monuments', 'latitude': 28.6129, 'longitude': 77.2295},
                {'xid': 'd3', 'name': 'Qutub Minar', 'kinds': 'historic', 'latitude': 28.5244, 'longitude': 77.1855},
            ]

        # Chennai specific mocks
        if 13.0 <= lat <= 13.1 and 80.2 <= lon <= 80.3:
            return [
                {'xid': 'c1', 'name': 'Marina Beach', 'kinds': 'beaches', 'latitude': 13.0445, 'longitude': 80.2824},
                {'xid': 'c2', 'name': 'Kapaleeshwarar Temple', 'kinds': 'temples', 'latitude': 13.0333, 'longitude': 80.2707},
            ]
        
        return [
            {'xid': 'm1', 'name': 'Famous Museum', 'kinds': 'museums', 'latitude': lat + 0.001, 'longitude': lon + 0.001},
            {'xid': 'm2', 'name': 'Grand Park', 'kinds': 'parks', 'latitude': lat - 0.001, 'longitude': lon - 0.001},
            {'xid': 'm3', 'name': 'Historic Tower', 'kinds': 'historic', 'latitude': lat + 0.002, 'longitude': lon - 0.002},
        ]
