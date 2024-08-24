import requests
import os
from prettytable import PrettyTable
# import asyncio
# import websockets

class CryptoCurrency:
    base_url = "https://rest.coinapi.io/v1/exchangerate"
    headers = {
        "X-CoinAPI-Key": os.environ.get("api_key")
    }
    currency = "INR"
    prices = []
    def __init__(self, symbol):
        self.symbol = symbol
        self.add_prices_to_list()

    @property
    def complete_url(self):
        return f"{CryptoCurrency.base_url}/{self.symbol}/{CryptoCurrency.currency}"

    @property
    def price(self):
        req = requests.get(self.complete_url, headers=CryptoCurrency.headers).json()
        return round(float(req.get('rate')),2)

    def add_prices_to_list(self):
        CryptoCurrency.prices.append(
            [self.symbol, self.price]
        )

    @staticmethod
    def prices_table():
        pt = PrettyTable(["Crypto Name", "Prices"])
        pt.add_rows(CryptoCurrency.prices)
        return pt

    @staticmethod
    def clean_prices():
        CryptoCurrency.prices.clear()

    @staticmethod
    def show_prices():
        print(CryptoCurrency.prices_table())