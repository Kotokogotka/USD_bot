# Проект "Курс доллара в боте"

Этот проект представляет собой Telegram бота, который предоставляет информацию о текущем курсе доллара в рублях. Пользователи могут получить актуальные данные о курсе доллара на сегодня, подписаться на ежедневные обновления курса и узнать курс на выбранную дату.

## Структура проекта

- **`main.py`**: Основной файл с логикой бота и инициализацией диспетчера.
- **`user_handler.py`**: Модуль с обработчиками сообщений и состояний пользователя.
- **`models.py`**: Модуль с определением классов данных (например, `Currency`) и обработчиком Redis (например, `RedisRateHandler`).
- **`lexiconRU.py`**: Модуль с текстовыми строками, используемыми в боте.
- **`script_currency.py`**: Модуль для получения актуального курса доллара из внешнего источника.
- **`keyboards.py`**: Модуль с клавиатурами, используемыми в боте.
- **`config.py`**: Модуль с конфигурацией бота и функцией загрузки конфигурации.
- **`.env`**: Файл с переменными окружения (например, `BOT_TOKEN`).

## Установка и Запуск

### Клонирование репозитория:

```sh
git clone https://github.com/Kotokogotka/USD_bot
```

### Установка зависимостей:

```sh
pip install -r requirements.txt
```

### Настройка конфигурации:

Создайте файл `.env` и добавьте туда переменные окружения, включая `BOT_TOKEN` для доступа к API Telegram.

### Запуск бота:

```sh
python main.py
```

## Использование

- Отправьте команду `/start` боту в Telegram, чтобы начать работу.
- Используйте команду `/dollar`, чтобы узнать текущий курс доллара.
- Используйте команду `/history`, чтобы получить информацию о курсе доллара на выбранную дату.
- Используйте команду `/subscribe`, чтобы подписаться на ежедневные обновления курса доллара.

## Работа с Redis

Для хранения данных о курсе доллара и подписках пользователей используется Redis, быстрое и надежное хранилище данных. Для работы с Redis в проекте используется класс `RedisRateHandler` из модуля `models.py`.

Пример использования RedisRateHandler:

```python
# Создание объекта RedisRateHandler
radis_handler = RedisRateHandler(host='localhost', port=6379)

# Добавление данных о курсе доллара в Redis
currency = Currency(name="Dollar", code="USD", price=75.0, date=datetime.now(), sub=True)
await radis_handler.add_currency(currency)

# Получение данных о курсе доллара из Redis на выбранную дату
usd_rate = await radis_handler.get_currency('USD', '01-01-2023')

# Установка подписки на рассылку для пользователя
user_id = 12345
user_key = f"user:{user_id}"
await radis_handler.set_user_subscription(user_key, True)

# Проверка подписки пользователя
is_subscribed = await radis_handler.get_user_subscription(user_key)
```

## Как внести свой вклад

1. Форкните проект (https://github.com/Kotokogotka/USD_bot/fork)
2. Создайте свою ветку (`git checkout -b feature/новая_функция`)
3. Зафиксируйте свои изменения (`git commit -am 'Добавить новую функцию'`)
4. Загрузите ветку (`git push origin feature/новая_функция`)
5. Создайте запрос на включение изменений (Pull Request)