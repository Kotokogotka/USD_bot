
from datetime import datetime
from script_currency import cours_dollar_to_rub
from lexiconRU import commands
from keyboards import sub_kd
from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from model import RedisRateHandler
from aiogram.fsm.state import default_state
from aiogram.types import Message
from aiogram.filters.state import StatesGroup, State, StateFilter
from model import Currency



router: Router = Router()

# Подключение к базе данных
radis_handler = RedisRateHandler(host='localhost', port=6379)
class HistoryForm(StatesGroup):
    data = State()


@router.message(Command('start'))
async def process_start_command(message: Message):
    await message.answer(text=commands['/start'])


@router.message(Command('help'))
async def process_start_command(message: Message):
    await message.answer(text=commands['/help'])


@router.message(Command('dollar'))
async def process_dollar_command(message: Message):
    # Получаем данные о курсе доллара из внешнего источника
    usd_to_rub_rate = await cours_dollar_to_rub()

    if usd_to_rub_rate is not None:
        # Сохраняем данные о курсе доллара в базе данных Redis
        code = "USD"
        current_date = datetime.now()

        # Проверяем, подписан ли пользователь на рассылку
        chat_id = message.chat.id
        user_key = f"user:{chat_id}"
        is_subscribed = await radis_handler.get_user_subscription(user_key)

        currency = Currency(name="Dollar", code=code, price=usd_to_rub_rate, date=current_date, sub=is_subscribed)
        await radis_handler.add_currency(currency)

        # Формируем ответ для пользователя
        response_text = f"Курс доллара на сегодня: {usd_to_rub_rate} RUB"
    else:
        response_text = "Извините, не удалось получить данные о курсе доллара на сегодня."

    # Отправляем ответ пользователю с клавиатурой
    await message.answer(response_text, reply_markup=sub_kd)


# Обработчик колбеков от кнопок инлайн-клавиатуры
@router.callback_query(lambda c: c.data == 'subscription')
async def handle_subscribe_callback(callback_query: types.CallbackQuery):
    # Получаем идентификатор пользователя, который нажал кнопку
    user_id = callback_query.from_user.id

    # Устанавливаем подписку на рассылку для пользователя в базе данных Redis
    user_key = f"user:{user_id}"
    await radis_handler.set_user_subscription(user_key, True)

    # Отправляем сообщение пользователю об успешной подписке
    await callback_query.answer('Вы успешно подписались на рассылку. Курс доллара будет отправлен вам каждый день в 10:00.')



@router.message(Command('Подписаться'))
async def process_subscribe_command(message: Message):
    # Обновляем параметр подписки в базе данных Redis для текущего пользователя
    chat_id = message.chat.id
    user_key = f"user:{chat_id}"
    await radis_handler.set_user_subscription(user_key, True)
    await message.answer("Вы успешно подписались на рассылку. Курс доллара будет отправлен вам каждый день в 10:00.")


@router.message(Command('commands'))
async def process_echo_command(message: Message):
    await message.reply('Доступные команды: \n\n'
                        '/start - начать работу с ботом\n\n'
                        '/dollar - узнать стоимость доллара\n\n'
                        '/help - Информация по работе бота\n\n'
                        '/history - Информация о ранее выполненных запросах курса доллара')


@router.message(Command('history'), StateFilter(default_state))
async def process_history_command(message: Message, state: FSMContext):
    await message.answer(text=commands['/history'])
    # Состояние ожидания ввода даты
    await state.set_state(HistoryForm.data)


@router.message(StateFilter(HistoryForm.data))
async def process_history_date(message: Message, state: FSMContext):
    user_input = message.text

    try:
        user_date = datetime.strptime(user_input, '%d-%m-%Y')
        usd_rate = await radis_handler.get_currency('USD', user_date.strftime('%d-%m-%Y'))
        if usd_rate:
            await message.answer(f"Курс доллара на {user_date.strftime('%d-%m-%Y')}: {usd_rate.price} RUB")
        else:
            await message.answer('На выбранную дату вы не запрашивалии ранее курс валюты')

    except ValueError:
        await message.answer(f'Некорректный формат даты, введите дату в формате дд-мм-гггг, нажмите еще раз /history')

    await state.clear()


