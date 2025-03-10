from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from src.database.crud import add_user, get_users_list, save_message, get_user_messages
from src.logs import getLogger

router = Router(name=__name__)
logger = getLogger(__name__)


@router.message(CommandStart())
async def command_start(message: Message):
    await add_user(message.from_user.id, message.from_user.username)


@router.message(Command("help"))
async def command_help(message: Message):
    await message.reply("""
/help - вывести все доступные команды,
/users - вывести список всех участников,
/my_messages - вывести список ваших сообщений.
    """)


@router.message(Command("users"))
async def command_users(message: Message):
    users_list = await get_users_list()
    text = "Список участников:\n"
    for c, i in enumerate(users_list, 1):
        text += f"User {c}: {i.id}\n"
    await message.reply(text)


@router.message(Command("my_messages"))
async def command_my_messages(message: Message):
    message_list = await get_user_messages(message.from_user.id)
    text = "Список ваших сообщений:\n"
    for c, msg in enumerate(message_list, 1):
        date = f"{msg.created_at.year}.{msg.created_at.month}.{msg.created_at.day} {msg.created_at.hour}:{msg.created_at.minute}"
        text += f"{date} | {msg.text}\n"
    await message.reply(text)


@router.message(lambda message: not message.text.startswith("/"))
async def on_message(message: Message):
    await save_message(message.message_id, message.text, message.from_user.id, message.date)
