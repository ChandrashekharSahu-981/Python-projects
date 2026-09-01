import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

my_email = os.getenv("EMAIL")
my_password = os.getenv("PASSWORD")

def notify(cheap_flights, first_name, email):
    message = f"Hi {first_name}!\n\n"
    message += "Cheap flights found!\n\n"
    for flight in cheap_flights:
        message += (
            f"Destination: {flight['city']}\n"
            f"Flight Price: Rs. {flight['flight_price']}\n"
            f"Target Price: Rs. {flight['target_price']}\n"
            f"You Save: Rs. "
            f"{flight['target_price'] - flight['flight_price']}\n"
            f"\n--------------------\n\n"
        )
                    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject: Cheap Flight Found!\n\n{message}"
        )
        