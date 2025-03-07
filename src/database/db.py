import psycopg2
from src.config import settings
from typing import Tuple
from configparser import NoOptionError


class Database:
    def __init__(self):
        try:
            self.host = settings.db.host
            self.user = settings.db.user
            self.password = settings.db.password
            self.database = settings.db.db_name

        except NoOptionError as e:
            raise Exception(f"DB configuration error: {e}")

    def _connect(self):
        return psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def execute_query(self, query: str, params: Tuple = ()) -> None:
        """Выполняет запрос без возврата данных (INSERT, UPDATE, DELETE)."""
        with self._connect() as con:
            with con.cursor() as cur:
                cur.execute(query, params)

    def fetch_all(self, query: str, params: Tuple = ()) -> None:
        """Выполняет SELECT запрос и возвращает записи"""
        with self._connect() as con:
            with con.cursor() as cur:
                cur.execute(query, params)
                return cur.fetchall()

    def fetch_one(self, query: str, params: Tuple = ()) -> None:
        """Выполняет SELECT запрос и возвращает запись"""
        with self._connect() as con:
            with con.cursor() as cur:
                cur.execute(query, params)
                return cur.fetchone()


db = Database()
