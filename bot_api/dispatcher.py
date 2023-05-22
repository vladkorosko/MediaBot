from aiogram import Bot, Dispatcher, types

import bot_api.config as config


class MediaManagerBot:
    def __init__(self):
        self.dp = Dispatcher(Bot(token=config.BOT_TOKEN, parse_mode="HTML"))


bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
