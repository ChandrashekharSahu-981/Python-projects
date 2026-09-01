import requests
from dotenv import load_dotenv
import os

load_dotenv()

sheety_data_url = os.getenv("SHEETY_ENDPOINT_DATA")
sheety_data_token = os.getenv("SHEETY_TOKEN_DATA")
sheety_data_headers = {
    "Authorization": f"Bearer {sheety_data_token}"
}

def get_data():
    response = requests.get(url=sheety_data_url,headers=sheety_data_headers)
    response.raise_for_status()
    data = response.json()["sheet1"]
    return data

sheety_user_url = os.getenv("SHEETY_ENDPOINT_USER")
sheety_user_token = os.getenv("SHEETY_TOKEN_USER")
sheety_user_headers = {
    "Authorization": f"Bearer {sheety_user_token}"
}

def get_users():
    response = requests.get(url=sheety_user_url,headers=sheety_user_headers)
    response.raise_for_status()
    data = response.json()["users"]
    return data
