from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.src.bot_app import dp
from .app import bot
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


@dp.callback_query_handler(lambda x: x.data in ['MAS', 'FEM', 'GEN'], state=GameStates.random_ten)
async def button_click_callback(callback_query: types.CallbackQuery, state: FSMContext):
    # bot of Bot object
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    async with state.proxy() as data:
        if answer == data.get(answer):
            response = await get_random()
            data['step'] += 1
            data['answer'] = response.get('gender')
            data['word'] = response.get('word')
            if data['step'] > 10:
                await bot.send_message(callback_query.from_user.id, "Game is Over!!")
                await GameStates.start.set()
            else:
                await bot.send_message(callback_query.from_user.id,
                                       "Yes\n" + f"{data['step']} of 10. or your word {data['word']}",
                                       reply_markup=inline_kb)
        else:
            await bot.send_message(callback_query.from_user.id,
                                   "No\n",
                                   reply_markup=inline_kb)
