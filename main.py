import asyncio
import logging
from aiogram import Bot, Dispatcher
import user_handler
from config import load_config, Config

# Инициализация логирования
logger = logging.getLogger(__name__)


# Конфигурация логирования и запуска бота

async def main():
    # Конфигурация логов
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info('Start bot!')

    # Загрузка конфигураций в переменную
    config: Config = load_config()

    # Инициализация бота и диспатчера
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')

    dp: Dispatcher = Dispatcher()

    # Регистрация роутера в диспатчере
    dp.include_router(user_handler.router)

    # Пропуск апдейтов и запуск пулинга
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())