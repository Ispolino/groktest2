from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from src.database.db import async_engine, AsyncSessionLocal
from src.database.models import Base, UserModel


async def init_db():
    """Инициализация базы данных"""
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def add_user(user_id: int, username: str = None):
    """Добавление юзера в бд"""
    async with AsyncSessionLocal() as session:
        async with session.begin():
            stmt = insert(UserModel).values(id=user_id, username=username)
            stmt = stmt.on_conflict_do_nothing(index_elements=['id'])
            await session.execute(stmt)


async def get_users_list():
    """Получение списка юзеров"""
    async with AsyncSessionLocal() as session:
        stmt = select(UserModel)
        result = await session.execute(stmt)
        return result.scalars()

