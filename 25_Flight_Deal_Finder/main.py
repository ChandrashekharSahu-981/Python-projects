from data_manager import get_data, get_users
from flight_manager import search_flights
from notification import notify

destinations = get_data()

print("Welcome to FLIGHT DEAL FINDER!")
departure = input("Enter your departure airport IATA code: ").upper()
date = input("Enter departure date (YYYY-MM-DD): ")

cheap_flights = []
for destination in destinations:
    city = destination["city"]
    iata_code = destination["iataCode"]
    target_price = destination["targetPrice"]

    flight_price = search_flights(
        departure,
        iata_code,
        date,
    )
    
    if flight_price <= target_price:
        cheap_flights.append({
            "city": city,
            "flight_price": flight_price,
            "target_price": target_price
        })
if cheap_flights:
    users = get_users()
    for user in users:
        notify(
            cheap_flights,
            user["firstName"],
            user["email"]
        )
    print("Email has been successfully sent to all users!")
else:
    print("No cheap flights found!")
        

