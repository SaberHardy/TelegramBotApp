from aiogram.utils import executor

from bot.src.bot_app.app import dp

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
