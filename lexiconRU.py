from datetime import datetime
from script_currency import cours_dollar_to_rub

current_datetime = datetime.now()
current_data = current_datetime.date()
dollar = cours_dollar_to_rub()
currency = {
    'Dollar': 'USD'
}

commands = {
    '/start': f'Данный бот подскажет курс доллара на {current_data}\n\nКликай на /dollar',
    '/dollar': f'Цена одного доллара на {current_data} составляет {dollar} рублей',
    '/history': 'Введите дату в формате: день месяц год (11-11-2011)',
    '/help': f'/start - Осуществляет запуск бота\n\n'
             f'/dollar - Показывает курс доллара с 00:00:01 сегодняшнего дня до 00:00:00 следующего дня\n\n,'
             f'/history - Предоставляет курс доллара на выбранную дату в формате дд-мм-гггг\n\n'
             f'/commands - показывает список доступных команд\n\n'
}
