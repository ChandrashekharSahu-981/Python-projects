from dotenv import load_dotenv
import requests
import smtplib
import os

load_dotenv()

owm_api_key = os.getenv("API_KEY")
my_email = os.getenv("EMAIL")
my_password = os.getenv("PASSWORD")

weather_url = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat" : 18.443599,
    "lon" : 73.895774,
    "appid": owm_api_key,
    "cnt" : 4
}

response = requests.get(url=weather_url, params=parameters)
response.raise_for_status()
weather_data = response.json()

for hour_data in weather_data["list"]:
    condition = hour_data["weather"][0]["id"]
    
    if condition < 700:
        rain_time = hour_data["dt_txt"]
        
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password)

            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"""Subject: Weather Alert\n\nIt's going to rain around {rain_time}.Remember to take an umbrella!"""
            )
        break