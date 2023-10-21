from dataclasses import dataclass
import os
from environs import Env

@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм боту

@dataclass
class Config:
    tg_bot: TgBot

# Функция загрузки конфигурации
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env("BOT_TOKEN")))

# Определение переменных окружения после вызова функции load_config
ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))
POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'
