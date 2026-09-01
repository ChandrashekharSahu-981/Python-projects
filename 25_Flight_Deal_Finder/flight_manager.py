import requests
from dotenv import load_dotenv
import os

load_dotenv()

serpapi_key = os.getenv("SERPAPI_KEY")
serpapi_endpoint = os.getenv("SERPAPI_ENDPOINT")


def search_flights(departure, arrival, date):
    params = {
        "engine": "google_flights",
        "departure_id": departure,
        "arrival_id": arrival,
        "type": "2",
        "outbound_date": date,
        "currency": "INR",
        "api_key": serpapi_key
    }


    response = requests.get(
        url=serpapi_endpoint,
        params=params
    )
    response.raise_for_status()
    flight_data = response.json()
    return flight_data["price_insights"]["lowest_price"]

