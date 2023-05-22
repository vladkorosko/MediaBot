from aiogram import executor
from bot_api.handlers.actions import *

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
