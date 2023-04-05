import json
import requests
from config import currency_list


class CurrencyException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise CurrencyException('Валюты должны быть разными для перевода из одной в другую.')

        if amount.isdigit():
            int(amount)
        else:
            raise CurrencyException('Количество валюты должно быть целым числом.')

        try:
            currency_list[quote] = currency_list[quote]
        except KeyError:
            raise CurrencyException(f'Не удалось обработать валюту: {quote}')

        try:
            currency_list[base] = currency_list[base]
        except KeyError:
            raise CurrencyException(f'Не удалось обработать валюту: {base}')

        r = requests.get(
            f'https://currate.ru/api/?get=rates&pairs={currency_list[quote]}{currency_list[base]}&key=cef9615ba5131ed58b15b1840241738d')

        cur = currency_list[quote] + currency_list[base]
        total_base = round(float(json.loads(r.content)['data'][cur]) * int(amount), 2)

        return total_base
