from src.database.db import db


def init_db():
    """Инициализация базы данных"""
    db.execute_query("""
    CREATE TABLE IF NOT EXISTS users(
        id INT PRIMARY KEY,
        username TEXT DEFAULT NULL
    )
    """)


def add_user(user_id: int, username: str = None):
    """Добавление юзера в бд"""
    db.execute_query("""
    INSERT INTO users (id, username)
    VALUES (%s, %s)
    ON CONFLICT (id) DO NOTHING;
    """, (user_id, username))


def get_users_list():
    """Получение списка юзеров"""
    return db.fetch_all("SELECT * FROM users")

