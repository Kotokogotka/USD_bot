import redis
from datetime import datetime
import re


class Currency:
    def __init__(self, name: str, code: str, price: float, date: datetime, sub: bool):
        self.name = name
        self.code = code
        self.price = price
        self.date = date
       # self.sub = sub
class RedisRateHandler:
    def __init__(self, host: str, port: int, db_num=0):
        self.redis = redis.Redis(host=host, port=port, db=db_num, decode_responses=True)

    async def add_currency(self, currency: Currency) -> None:
        key = f"{currency.code}:{self.convert_to_date(currency.date)}"
        data = f"{currency.name}:{currency.price}:{currency.sub}"
        return self.redis.set(key, data)

    async def set_user_subscription(self, username: str, is_subscribed: bool) -> None:
        # Обновляем параметр подписки пользователя в базе данных Redis
        await self.redis.set(username, is_subscribed)

    async def get_user_subscription(self, user_key: str) -> bool:
        # Получаем параметр подписки пользователя из базы данных Redis
        subscribed = self.redis.hget(user_key, 'sub')
        # Если пользователь подписан, возвращаем True, иначе False
        return bool(subscribed) if subscribed else False

    async def get_currency(self, code, date):
        # Парсим строку с датой в объект datetime
        user_date = datetime.strptime(date, '%d-%m-%Y')
        rate_value = self.redis.get(f"{code}:{self.convert_to_date(user_date)}")
        if rate_value is not None:
            # Используем регулярное выражение для извлечения числа из строки
            price_match = re.search(r'\d+\.\d+', rate_value)
            if price_match:
                price = float(price_match.group())
                return Currency("Dollar", code, price, user_date)
        return None

    @staticmethod
    def convert_to_date(date: datetime) -> str:
        return date.strftime('%d-%m-%Y')
