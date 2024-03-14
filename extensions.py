import requests
import json
from config import keys
class APIException (Exception):
    pass

class CurrencyConvertor:
    @staticmethod
    def get_price(quote:str,base:str,amount:str):


        if quote == base:
            raise APIException ('Валюты должны быть разными.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException (f'Не удалось обработать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException (f'Не удалось обработать количество {amount}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException (f'Не удалось обработать валюту {base}')
        print(base_ticker,quote_ticker,amount)

        r = requests.get(f'https://v6.exchangerate-api.com/v6/f881a6501355f2c41a378e8e/pair/{quote_ticker}/{base_ticker}')
        print(json.loads(r.content)["conversion_rate"])

        return json.loads(r.content)["conversion_rate"]*amount
        #return