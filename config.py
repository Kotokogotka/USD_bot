from dataclasses import dataclass
from environs import Env
from dotenv import load_dotenv


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

# Загрузите переменные окружения из файла .env
load_dotenv()
