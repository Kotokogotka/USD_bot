import redis
from datetime import datetime
import re


class Currency:
    def __init__(self, name: str, code: str, price: float, date: datetime):
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
