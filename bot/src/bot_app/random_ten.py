from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.src.bot_app import dp
from .data_fetcher import get_random
from .keyboards import inline_kb
from .states import GameStates


@dp.message_handler(commands="train_ten", state="*")
async def train_ten(message: types.Message, state: FSMContext):
    await GameStates.random_ten.set()
    results = await get_random()
    # to remember which word we are in
    async with state.proxy() as data:
        data['step'] = 1
        data['answer'] = results.get('gender')
        data['word'] = results.get('word')

        await message.reply(f"{data['step']} of 10 from {data['word']}", reply_markup=inline_kb)

# @dp.message_handler(commands=["train_all"])
# async def train_all(message: types.Message):
#     await message.reply("We are training all messages!")
