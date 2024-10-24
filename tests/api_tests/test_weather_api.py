# Docs can be found here
# https://openweathermap.org/current#geocoding
import os

import pytest
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
# API_KEY="4fe73cf039dee9c1917ceac20dc0d713"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@pytest.mark.parametrize("city, country, expected_city", [
    ("London", "uk", "London"),
    ("Paris", "fr", "Paris"),
    ("New York", "us", "New York"),
])
def test_get_weather_by_city(city, country, expected_city):
    url_to_test = f"{BASE_URL}?q={city},{country}&appid={API_KEY}"
    response = requests.get(url_to_test)  # send request to the server, receive response

    assert response.status_code == 200
    json_response = response.json()
    assert json_response["name"] == expected_city
    assert "weather" in json_response
    assert "main" in json_response
    assert "temp" in json_response["main"]

def test_get_weather_by_city_not_found():
    response = requests.get(f"{BASE_URL}?q=InvalidCity&appid={API_KEY}")
    assert response.status_code == 404
    json_response = response.json()
    assert json_response["message"] == "city not found"
