import requests
import json
from CurrencyFactory import Currency


class CurrencyApi:
    URL_BASE = 'https://rest.coinapi.io/v1/assets'
    API_KEY = '74D8678B-4A91-4A77-B275-24A466462AB0'

    def get_crypto(self, currency_id):
        try:
            url = f'{self.URL_BASE}/{currency_id}'
            headers = {'X-CoinAPI-Key': self.API_KEY}
            request = requests.get(url, headers=headers)
            response = request.content.decode()
            json_currency = json.loads(response)
            currency = Currency(json_currency)
            return currency
        except Exception:
            return False


class CurrencyConverter:
    def __init__(self):
        self.currency_api = CurrencyApi()

    def convert(self, currency_from, currency_to, currency_amount):
        currency_amount = float(currency_amount)
        if currency_from == 'USD':
            currency_to = self.currency_api.get_crypto(currency_to)
            result = (1 / float(currency_to.price_usd)) * currency_amount
        elif currency_to == 'USD':
            currency_from = self.currency_api.get_crypto(currency_from)
            result = float(currency_from.price_usd) * currency_amount
        else:
            currency_from = self.currency_api.get_crypto(currency_from)
            currency_to = self.currency_api.get_crypto(currency_to)
            result = (float(currency_from.price_usd) / float(currency_to.price_usd)) * currency_amount

        return f'{result:.2f}'


'''result = CurrencyConverter().convert('BTC', 'EUR', 100)
print(result)'''


'''real = CurrencyApi().get_crypto('EUR')
print(real.price_usd)'''


'''https://docs.coinapi.io/?python#list-all-assets-get'''
