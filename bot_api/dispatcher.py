from aiogram import Bot, Dispatcher, types

import config


class MediaManagerBot:
    def __init__(self):
        self.dp = Dispatcher(Bot(token=config.BOT_TOKEN, parse_mode="HTML"))
        self.is_video_menu = False
        self.is_photo_menu = False
        self.is_crop_menu = False


bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
