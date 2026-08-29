from dotenv import load_dotenv
import requests
import smtplib
import os

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

stock_api_key = os.getenv("STOCK_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
my_email = os.getenv("EMAIL")
my_password = os.getenv("PASSWORD")

news_endpoint = "https://newsapi.org/v2/everything"
news_params = {
    "apiKey" : news_api_key,
    "q": f"{COMPANY_NAME} AND (stock OR shares)",
    "language": "en",
    "sortBy": "publishedAt"
}

stock_endpoint = "https://www.alphavantage.co/query"
stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : stock_api_key
}

try: 
    stock_response = requests.get(url=stock_endpoint, params=stock_params)
    stock_response.raise_for_status()
    stock_data = stock_response.json()["Time Series (Daily)"]
except requests.exceptions.RequestException:
    print("Unable to connect to Alpha Vantage.")
    exit()
except KeyError:
    print("Stock data is unavailable. The API limit may have been reached. Please try again later!")
    exit()

stock_data_list = [value for (key, value) in stock_data.items()]

yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]

difference = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = (difference / float(day_before_yesterday_closing_price)) * 100

if abs(diff_percent) > 1:
    news_response = requests.get(url=news_endpoint, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    
    formatted_articles = [f"Headline: {article['title']}. Brief: {article['description']}. \nURL: {article['url']}" for article in three_articles]

    email_body = (
        f"{STOCK_NAME}: {diff_percent:+.2f}%\n"
        f"Yesterday's closing price: ${yesterday_closing_price}\n"
        f"Previous closing price: ${day_before_yesterday_closing_price}\n\n"
        + "\n\n".join(formatted_articles)
    )

    email_body = email_body.encode("ascii", "ignore").decode("ascii")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Stock News\n\n{email_body}"         
        )
    