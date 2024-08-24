from crypto_scraper import CryptoCurrency
import time
import os


if __name__ == '__main__':
    CryptoCurrency.currency = "USD"
    while True:
        symbol1 = CryptoCurrency(symbol='BTC')
        symbol2 = CryptoCurrency(symbol='ETH')
        symbol3 = CryptoCurrency(symbol='DOGE')

        os.system("cls")
        CryptoCurrency.show_prices()
        CryptoCurrency.clean_prices()
        time.sleep(3)
