from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexiconRU import currency

kb = [[
    KeyboardButton(text=currency['Dollar'])
]]

keyboard = ReplyKeyboardMarkup(keyboard=kb)

