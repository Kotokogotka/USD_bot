from gino import Gino
from sqlalchemy import Column, BigInteger, String, REAL, Date
import datetime
from asyncpg import UniqueViolationError
from config import Config
from main import Dispatcher

db = Gino()

class User(db.Model):
    __tablename__ = 'bot_test'

    user_id = Column(BigInteger(), primary_key=True)
    currenc = Column(String(10))
    value = Column(REAL)
    data = Column(Date())
    created_at = db.Column(db.DateTime(True), server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=db.func.now())

async def on_startup(dp: Dispatcher):
    print('Установка связи с PostgreSQL')
    await db.set_bind(Config.POSTGRES_URI)
    await db.gino.create_all()

async def add_user(user_id: int, currenc: str, value: float, data: str):
    try:
        user = User(user_id=user_id, currenc=currenc, value=value, data=data)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')

async def select_all_user():
    users = await User.query.gino.all()
    return users

async def count_user():
    count = db.func.count(User.user_id).gino.scalar()
    return count

async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user
