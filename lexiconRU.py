from datetime import datetime
from script_currency import cours_dollar_to_rub

current_datetime = datetime.now()
current_data = current_datetime.date()

currency = {
    'Dollar': 'USD'
}

commands = {
    '/start': f'Данный бот подскажет курс доллара на {current_data}\n\nКликай на /dollar',
    '/dollar': f'Цена одного доллара на {current_data} составляет {cours_dollar_to_rub()} рублей',
    '/history': f'Введите дату в формате: день месяц год (11 11 2011)'
}

