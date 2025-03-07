import psycopg2
from typing import Tuple
from configparser import NoOptionError
from src.config import settings
from src.logs import getLogger

logger = getLogger(__name__)


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
        try:
            return psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database)
        except psycopg2.errors.OperationalError as e:
            logger.error(f"connection error: {e}")

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
