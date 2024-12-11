# скачиваем необходимые библиотеки: Aiogram 3x, sqlalchemy, asyncpg, python-dotenv
import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from app.handlers import admin


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(admin)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
