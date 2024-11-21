
import requests
import pandas as pd
from pytrends.request import TrendReq

def fetch_google_trends_data(['Bitcoin',
'Ethereum',
'BNB',
'Solana',
'XRP',
'Dogecoin',
'Cardano',
'Polkadot',
'Chainlink',
'Litecoin',
'Uniswap',
'Filecoin',
'Fetch.ai',
'Monero',
'Singularitynet',
'Kezos',
'Kucoin',
'Pancakeswap',
'oasis network',
'ocean protocol'], '2024-01-01', '2024-11-01'):
    pytrends = TrendReq()
    pytrends.build_payload(['Bitcoin',
'Ethereum',
'BNB',
'Solana',
'XRP',
'Dogecoin',
'Cardano',
'Polkadot',
'Chainlink',
'Litecoin',
'Uniswap',
'Filecoin',
'Fetch.ai',
'Monero',
'Singularitynet',
'Kezos',
'Kucoin',
'Pancakeswap',
'oasis network',
'ocean protocol'], cat=0, timeframe=f"{'2024-01-01'} {'2024-11-01'}", geo='', gprop='')
    data = pytrends.interest_over_time()
    data.reset_index(inplace=True)
    return data

def fetch_crypto_data(https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc):
    response = requests.get(https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

