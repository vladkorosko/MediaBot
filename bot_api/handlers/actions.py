from aiogram import types

from bot_api.dispatcher import dp
import bot_api.handlers.addion_functions as ad

from bot_api.handlers.photo_handler import crop_photo_handler
from bot_api.handlers.photo_handler import puzzle_photo_handler
from bot_api.handlers.photo_handler import resize_photo_handler
from bot_api.handlers.photo_handler import change_format_photo_handler

from get_extension import get_format as gf


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_photo = types.KeyboardButton("Photo")
    button_video = types.KeyboardButton("Video")

    markup.add(button_photo, button_video)

    # await msg.reply("Bot for photo and video editing", parse_mode="html", reply_markup=markup)

    await msg.reply("Bot for photo and video editing\n"
                    "Send photo with description 'puzzle (number of columns) to make puzzle")


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handler_photo_message(msg):
    if msg.caption is not None:
        command = msg.caption.split()
        file_name = "input"
        file_format = "jpg"
        if command[0] == 'crop' and len(command) == 5:
            if ad.is_integer(command[1]) and ad.is_integer(command[2]) and ad.is_integer(command[3]) and ad.is_integer(
                    command[4]):
                await crop_photo_handler("input", ".jpg", msg, command, types.ContentType.PHOTO)
            else:
                await msg.reply('Command "CROP": Wrong parameters')
        elif command[0] == 'puzzle' and len(command) == 2:
            if ad.is_integer(command[1]):
                await puzzle_photo_handler("input", ".jpg", msg, command, types.ContentType.PHOTO)
            else:
                await msg.reply('Command "PUZZLE": Wrong parameters')
        elif command[0] == 'resize' and len(command) == 3:
            if ad.is_integer(command[1]) and ad.is_integer(command[2]):
                await resize_photo_handler("input", ".jpg", msg, command, types.ContentType.PHOTO)
            else:
                await msg.reply('Command "RESIZE": Wrong parameters')
        elif command[0] == 'format' and len(command) == 2:
            await change_format_photo_handler("input", ".jpg", msg, command, types.ContentType.PHOTO)
        else:
            await msg.reply('Photo: Wrong command')
    else:
        await msg.reply('Command is absent')


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def puzzle_photo1(msg):
    if msg.document is not None:
        if msg.caption is not None:
            file_name, file_format = gf(msg.document.file_name)
            command = msg.caption.split()
            if command[0] == 'crop' and len(command) == 5:
                if ad.is_integer(command[1]) and ad.is_integer(command[2]) and ad.is_integer(
                        command[3]) and ad.is_integer(command[4]):
                    await crop_photo_handler(file_name, file_format, msg, command, types.ContentType.DOCUMENT)
                else:
                    await msg.reply('Command "CROP": Wrong parameters')
            elif command[0] == 'puzzle' and len(command) == 2:
                if ad.is_integer(command[1]):
                    await puzzle_photo_handler(file_name, file_format, msg, command, types.ContentType.DOCUMENT)
                else:
                    await msg.reply('Command "PUZZLE": Wrong parameters')
            elif command[0] == 'resize' and len(command) == 3:
                if ad.is_integer(command[1]) and ad.is_integer(command[2]):
                    await resize_photo_handler(file_name, file_format, msg, command, types.ContentType.DOCUMENT)
                else:
                    await msg.reply('Command "RESIZE": Wrong parameters')
            elif command[0] == 'format' and len(command) == 2:
                await change_format_photo_handler(file_name, file_format, msg, command, types.ContentType.DOCUMENT)
            else:
                await msg.reply('Photo: Wrong command')
        else:
            await msg.reply('Command is absent')
    else:
        await msg.reply('Command is absent')

    # await msg.document.download(msg.document.file_name)
    # puzzle_photo(msg.document.file_name, 16)
    # await msg.reply_document(open("result.jpg", "rb"))
    # await msg.reply("This is file")


@dp.message_handler(content_types=types.ContentType.ANY)
async def puzzle_photo1(msg):
    if msg.caption is not None:
        await msg.reply(":".join(msg.caption.split()))
    else:
        await msg.reply("404: not found")
