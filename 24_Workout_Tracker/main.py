from dotenv import load_dotenv
import os
from datetime import datetime as dt
import requests

load_dotenv()

# Personal information used by the Nutritionix API to calculate calories.
GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 170
AGE = 20

# Retrieve Nutritionix credentials from environment variables.
api_id = os.getenv("WORKOUT_API_ID")
api_key = os.getenv("WORKOUT_API_KEY")

# Nutritionix API endpoint.
base_url = "https://app.100daysofpython.dev"

# Get the workout description from the user.
user_input = input("What exercises you did today?\n")
workout_data = {
  "query": user_input,
  "weight_kg": WEIGHT_KG,                  
  "height_cm": HEIGHT_CM,                 
  "age": AGE,                        
  "gender": GENDER                 
}
# Send the workout description to the Nutritionix API.
post_endpoint = f"{base_url}/v1/nutrition/natural/exercise"
headers = {
    "x-app-id": api_id,
    "x-app-key": api_key
}

response = requests.post(url=post_endpoint, json=workout_data, headers=headers)
response.raise_for_status()
exercise_data = response.json()

# Retrieve the Sheety endpoint and authentication token.
sheety_endpoint = os.getenv("SHEETY_URL")
sheety_token = os.getenv("SHEETY_TOKEN")
sheety_headers = {
    "Authorization" : f"Bearer {sheety_token}"
}

today = dt.now()

# Add each exercise returned by Nutritionix to the Google Sheet.
for exercise in exercise_data["exercises"]:
    sheet_data = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=sheety_endpoint, json=sheet_data, headers=sheety_headers)
    sheet_response.raise_for_status()
    print("Workout successfully added to Google Sheets!")



