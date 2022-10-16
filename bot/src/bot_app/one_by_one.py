from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.src.bot_app import dp
from .app import bot
from .data_fetcher import get_random, get_next
from .keyboards import inline_kb
from .states import GameStates


@dp.message_handler(commands="train_all", state="*")
async def train_all(message: types.Message, state: FSMContext):
    await GameStates.all_words.set()
    results = await get_next(0)
    if not results:
        await GameStates.start.set()
        await message.reply("All are done!====")
        return
    # to remember which word we are in
    async with state.proxy() as data:
        data['step'] = 1
        data['pk'] = 1
        data['answer'] = results.get('gender')
        data['word'] = results.get('word')

        await message.reply(f"{data['step']} of all words {data['word']}", reply_markup=inline_kb)


# @dp.message_handler(commands=["train_all"])
# async def train_all(message: types.Message):
#     await message.reply("We are training all messages!")


@dp.callback_query_handler(lambda x: x.data in ['MAS', 'FEM', 'GEN'], state=GameStates.all_words)
async def button_click_callback_all(callback_query: types.CallbackQuery, state: FSMContext):
    # bot of Bot object
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    async with state.proxy() as data:
        print(f"all data are: {data}")
        if answer == data.get('answer'):
            await bot.send_message(callback_query.from_user.id, "Yes\n")
            response = await get_next(data.get("pk"))
            if response:
                data['step'] += 1
                data['answer'] = response.get('gender')
                data['word'] = response.get('word')
                data['pk'] = response.get('pk')
                await bot.send_message(callback_query.from_user.id,
                                       f"{data['step']} of all words {data['word']}",
                                       reply_markup=inline_kb)
            else:
                await bot.send_message(callback_query.from_user.id, "The Game is Over")
                await GameStates.start.set()
        else:
            await bot.send_message(callback_query.from_user.id,
                                   "No\n",
                                   reply_markup=inline_kb)
