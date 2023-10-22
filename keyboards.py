from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from lexiconRU import currency
from aiogram.types import BotCommand


kb = [[
    KeyboardButton(text=currency['Dollar'])
]]

keyboard = ReplyKeyboardMarkup(keyboard=kb)


# Создаем объекты инлайн-кнопок
button1 = InlineKeyboardButton(
    text='Подписаться',
    callback_data='subscription'
)

# Создаем объект инлайн-клавиатуры
sub_kd = InlineKeyboardMarkup(
    inline_keyboard=[[button1],
                     ])

# Создание списка команд
main_menu_command = [
    BotCommand(command='/start',
                description='Запуск бота'),
    BotCommand(command='/help',
                description='Справка по работе бота'),
    BotCommand(command='/dollar',
                description='Узнать курс доллара на сегодня'),
    BotCommand(command='/history',
                description='Узнать курс на ранее выбранную вами дату'),
    BotCommand(command='/contact',
                description='Написать разработчику бота')
    ]

