import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
UP = "🔺"
DOWN = "🔻"

ALPHA_ENDPOINT = "https://www.alphavantage.co/query"
ALPHA_KEY = os.environ.get("ALPHA_KEY")

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_KEY,
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = os.environ.get("NEWS_KEY")

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_KEY,
}

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

def check_stock_price():
    stock_price_response = requests.get(url=ALPHA_ENDPOINT, params=alpha_parameters)
    stock_data = list(stock_price_response.json()["Time Series (Daily)"].items())[:2]
    stock_difference = round((float(stock_data[0][1]["4. close"]) - float(stock_data[1][1]["4. close"])) / float(stock_data[1][1]["4. close"]) * 100, 2)
    direction = UP if stock_difference > 0 else DOWN
    if abs(stock_difference) > 5:
        news = get_news()
        send_message(direction, abs(stock_difference), news)

def get_news():
    new_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_data = new_response.json()["articles"][:3]
    articles = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in news_data]
    return articles

def send_message(direction, difference, news):
    msg = f"{STOCK} {direction}{difference}%\n"
    for i in news:
        msg += f"{i}\n\n"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+10123456789",
        body=f"{msg}",
        to="whatsapp:+910123456789",
    )

check_stock_price()
