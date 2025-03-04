from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router
from src.database.db import add_user_to_db, get_users_list

router = Router(name=__name__)


@router.message(CommandStart())
async def command_start(message: Message):
    add_user_to_db(str(message.from_user.id))


@router.message(Command("help"))
async def command_help(message: Message):
    await message.reply("""
/help - вывести все доступные команды,
/users - вывести список всех участников.
    """)


@router.message(Command("users"))
async def command_users(message: Message):
    users_list = get_users_list()
    text = "Список участников:\n"
    for index, user in enumerate(users_list, 1):
        text += f"User {index}: {user}"
    await message.reply(text)
