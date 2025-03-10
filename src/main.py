import asyncio
from aiogram import Bot, Dispatcher
from src.config import settings
from src.handlers.user import router
from src.database.crud import init_db

dp = Dispatcher()


async def main():
    bot = Bot(token=settings.telegram.token)
    await init_db()
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_routers(router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
