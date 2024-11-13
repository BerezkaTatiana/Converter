import json
import requests
from config import keys, API_KEY

class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось идентифицировать валюту: {base}')
        try:
            quote_ticker = keys[quote]
            if base == quote:
                raise APIException('Введенные валюты не должны быть одинаковыми')
        except KeyError:
            raise APIException(f'Не удалось идентифицировать валюту: {quote}')
        try:
            amount = float(amount)
            if amount <= 0:
                raise APIException(f'Пожалуйста, введите число больше 0 вместо {amount}')
        except ValueError:
            raise APIException(f'Пожалуйста, введите целое число вместо {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}&{API_KEY}')
        total_base = json.loads(r.content)[keys[quote]]
        return total_base
