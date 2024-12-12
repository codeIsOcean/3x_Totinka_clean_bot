import asyncpg  # Импортируем библиотеку для работы с PostgresSQL


class Database():
    def __init__(self, db_url: str):
        # Инициализация класса Database, передаем url базы данных
        # Параметры:
        # db_url (str): URL подключение к базе данных PostgresSQL
        self.db_url = db_url  # сохраняем url базы данных, чтобы использовать его для подключения
        # postgresql://user:password@localhost:5432/dbname

        self.pool = None  # Переменная для хранения объекта пула соединений. Изначально она None,
        # пока соединение не установлено


async def connect(self):
    '''Создает подключение к базе данных и сохраняет его в self.pool'''
    self.pool = await asyncpg.create_pool(self.db_url)  # создает пул соединений, используя URL базы данных


async def disconnect(self):
    '''Закрывает соединение с базой данных, если оно активно.'''
    if self.pool:  # Проверяем, существует ли соединение
        await self.pool.close()  # Закрываем пул соединений


async def create_tables(self):
    '''Создает таблицы forbidden_words и forbidden links, если они еще не существуют'''
    async with self.pool.acquire() as connection:  # Берёт одно соединение из пула для выполнения запросов.
        await connection.execute('''
        CREATE TABLE IF NOT EXISTS forbidden_words(
        id SERIAL PRIMARY KEY, 
        word TEXT NOT NULL UNIQUE
        );
        CREATE TABLE IF NOT EXISTS forbidden_links(
        id SERIAL PRIMARY KEY,
        link TEXT NOT NULL UNIQUE
        );
        ''')
