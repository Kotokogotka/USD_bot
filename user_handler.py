
from lexiconRU import commands
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from aiogram.fsm.state import default_state
from aiogram.types import Message
from aiogram.filters.state import StatesGroup, State, StateFilter

router: Router = Router()



@router.message(Command('start'))
async def process_start_command(message: Message):
    await message.answer(text=commands['/start'])


@router.message(Command('dollar'))
async def process_dollar_command(message: Message):
    await message.answer(text=commands['/dollar'])


@router.message(Command('command'))
async def process_echo_command(message: Message):
    await message.reply('Доступные команды: \n\n'
                        '/start - начать работу с ботом\n\n'
                        '/dollar - узнать стоимость доллара')


@router.message(Command('history'))
async def process_history_command(message: Message):
    await message.answer('Введите дату в формате дд-мм-гггг')



