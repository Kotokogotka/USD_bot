
import requests

async def cours_dollar_to_rub():
    url = 'https://v6.exchangerate-api.com/v6/c721151c598bd59a283b7ab5/latest/USD'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rub_data = data['conversion_rates']['RUB']
        return rub_data
    else:
        print('Не удалось получить данные')
        return None
