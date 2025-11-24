import time
import json
import requests
from kafka import KafkaProducer

API_KEY = "d4har2pr01qgvvc6rgggd4har2pr01qgvvc6rgh0"
BASE_URL = "https://finnhub.io/api/v1/quote"

SYMBOLS = ["AAPL", "MSFT", "TSLA", "GOOGL", "AMZN"]

producer = KafkaProducer(
    # ⚠️ FINAL CORRECT BOOTSTRAP SERVER
    bootstrap_servers=['localhost:29092'],
    # to convert python dictionary to json file
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def fetch__quote(symbol):
    # the entire url
    url = f"{BASE_URL}?symbol={symbol}&token={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        data["symbol"] = symbol
        # to get the present time in UTC format
        data["fetched_at"] = int(time.time())
        return data
    # incase we don't get any data then raise an exception
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
        return None

# metadata means data about the data
# to create an infinite while loop
while True:
    # to iterate through the symbols list of 5 companies
    for symbol in SYMBOLS:
        quote = fetch__quote(symbol)
        if quote:
            print(f"Producing: {quote}")
            # sending a topic that we created on kafka the website
            producer.send("stocks-quotes", value=quote)

    # to delay the loop for 6 secs because finnhub lets us run 6 requests per min which is 1 request per sec
    time.sleep(6)
