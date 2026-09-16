from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import smtplib
import os

load_dotenv()

my_email = os.getenv("EMAIL")
my_password = os.getenv("PASSWORD")

# Amazon product page
URL = "https://www.amazon.in/dp/B0F54GKQ38"

# Headers make the request look like a normal browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Send request and parse the HTML
response = requests.get(URL, headers=headers)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

# Extract product price and title
price = soup.find(name="span", class_="a-price-whole")
product_price = float(price.get_text().replace(",", ""))

product_title = soup.find(id="productTitle").get_text().strip()
product_title = product_title.encode("ascii", "ignore").decode()

# Ask the user for their desired price
target_price = float(input("Enter your target price: "))

# Send an email if the current price is below the target
if product_price <= target_price:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg = f"""Subject: Amazon Price Tracker
{product_title}
The current price is {product_price}, which is below your target price of {target_price}.""" 
        )
    print("Email sent successfully!")
else:
    print(f"Product price is {product_price}, which is higher than your target price {target_price}.")
    