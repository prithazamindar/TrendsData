
import requests
import pandas as pd
from pytrends.request import TrendReq

def fetch_google_trends_data(keywords, start_date, end_date):
    pytrends = TrendReq()
    pytrends.build_payload(keywords, cat=0, timeframe=f"{start_date} {end_date}", geo='', gprop='')
    data = pytrends.interest_over_time()
    data.reset_index(inplace=True)
    return data

def fetch_crypto_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

# Example Usage
# google_trends = fetch_google_trends_data(['Bitcoin', 'Ethereum'], '2020-01-01', '2023-01-01')
# crypto_data = fetch_crypto_data('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc')
