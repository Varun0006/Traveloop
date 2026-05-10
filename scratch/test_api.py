import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GEODB_API_KEY')
print(f"Testing with API Key: {api_key[:5]}...")

url = "https://geodb-cities-api.p.rapidapi.com/v1/geo/cities"
querystring = {"namePrefix": "Hyderabad", "limit": "5", "sort": "-population"}
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "geodb-cities-api.p.rapidapi.com"
}

try:
    response = requests.get(url, headers=headers, params=querystring, timeout=10)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
