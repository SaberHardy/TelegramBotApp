from aiogram import types

from bot.src.bot_app import dp


@dp.message_handler(commands=["train_ten"])
async def train_ten(message: types.Message):
    await message.reply("We are training ten messages!")


@dp.message_handler(commands=["train_all"])
async def train_all(message: types.Message):
    await message.reply("We are training all messages!")
