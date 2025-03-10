from datetime import datetime
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from src.database.db import async_engine, AsyncSessionLocal
from src.database.models import Base, User, Message


async def init_db():
    """Инициализация базы данных"""
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def add_user(user_id: int, username: str = None):
    """Добавление юзера в бд"""
    async with AsyncSessionLocal() as session:
        async with session.begin():
            stmt = insert(User).values(id=user_id, username=username)
            stmt = stmt.on_conflict_do_nothing(index_elements=['id'])
            await session.execute(stmt)


async def get_users_list():
    """Получение списка юзеров"""
    async with AsyncSessionLocal() as session:
        stmt = select(User)
        result = await session.execute(stmt)
        return result.scalars()


async def save_message(message_id: int, text: str, from_user_id: int, created_at: datetime):
    """Сохранение сообщения в бд"""
    async with AsyncSessionLocal() as session:
        async with session.begin():
            new_message = Message(id=message_id, text=text, user_id=from_user_id, created_at=created_at)
            session.add(new_message)


async def get_user_messages(user_id: int):
    """Получения списка сообщений юзера"""
    async with AsyncSessionLocal() as session:
        stmt = select(Message).where(Message.user_id == user_id)
        result = await session.execute(stmt)
        return result.scalars()

