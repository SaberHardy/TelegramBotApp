from aiogram import types
from aiogram.types import message

from .app import dp


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Hello we are working today!!")
