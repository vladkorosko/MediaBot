import os

from aiogram import types

from photo_manager.puzzle_photo import puzzle_photo
from photo_manager.crop_photo import crop_photo
from photo_manager.resize_photo import resize_photo

from bot_api.dispatcher import dp
import bot_api.handlers.addion_functions as ad


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_photo = types.KeyboardButton("Photo")
    button_video = types.KeyboardButton("Video")

    markup.add(button_photo, button_video)

    #await msg.reply("Bot for photo and video editing", parse_mode="html", reply_markup=markup)

    await msg.reply("Bot for photo and video editing\n"
                    "Send photo with description 'puzzle (number of columns) to make puzzle")


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handler_photo_message(msg):
    if msg.caption is not None:
        command = msg.caption.split()
        if command[0] == 'crop' and len(command) == 5:
            if ad.is_integer(command[1]) and ad.is_integer(command[2]) and ad.is_integer(command[3]) and ad.is_integer(
                    command[4]):
                await msg.reply("Cropping")
                name = "crop_" + str(msg.from_id) + '_' + str(msg.message_id) + ".jpg"
                await msg.photo[-1].download(name)
                error = crop_photo(name, int(command[1]), int(command[2]), int(command[3]), int(command[4]))
                os.remove(name)
                if error is None:
                    result = name[:-4:] + '_result.jpg'
                    await msg.reply_document(open(result, "rb"))
                    os.remove(result)
                else:
                    await msg.reply(error)
            else:
                await msg.reply('Command "CROP": Wrong parameters')
        elif command[0] == 'puzzle' and len(command) == 2:
            if ad.is_integer(command[1]):
                await msg.reply("Making puzzle")
                name = "puzzle_" + str(msg.from_id) + '_' + str(msg.message_id) + ".jpg"
                await msg.photo[-1].download(name)
                puzzle_photo(name, int(command[1]))
                os.remove(name)
                result = name[:-4:] + '_result.jpg'
                await msg.reply_document(open(result, "rb"))
                os.remove(result)
            else:
                await msg.reply('Command "PUZZLE": Wrong parameters')
        elif command[0] == 'resize' and len(command) == 3:
            if ad.is_integer(command[1]) and ad.is_integer(command[2]):
                await msg.reply("Resizing")
                name = "resize_" + str(msg.from_id) + '_' + str(msg.message_id) + ".jpg"
                await msg.photo[-1].download(name)
                error = resize_photo(name, int(command[1]), int(command[2]))
                os.remove(name)
                if error is None:
                    result = name[:-4:] + '_result.jpg'
                    await msg.reply_document(open(result, "rb"))
                    os.remove(result)
                else:
                    await msg.reply(error)
            else:
                await msg.reply('Command "PUZZLE": Wrong parameters')
        else:
            await msg.reply('Photo: Wrong command')
    else:
        await msg.reply('Command is absent')


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def puzzle_photo1(msg):
    if msg.document is not None:
        if msg.caption is not None:
            command = msg.caption.split()
            if command[0] == 'crop' and len(command) == 5:
                if ad.is_integer(command[1]) and ad.is_integer(command[2]) \
                        and ad.is_integer(command[3]) and ad.is_integer(command[4]):
                    await msg.reply("Cropping")
                else:
                    await msg.reply('Command "CROP": Wrong parameters')
            elif command[0] == 'puzzle' and len(command) == 2:
                if ad.is_integer(command[1]):
                    await msg.reply("Making puzzle")
                    parse = list(msg.document.file_name.split('.'))
                    name = "input_" + str(msg.from_id) + '_' + str(msg.message_id) + '.' + parse[-1]
                    await msg.document.download(name)
                    puzzle_photo(name, int(command[1]))
                    os.remove(name)
                    result = name[:-4:] + '_result.jpg'
                    await msg.reply_document(open(result, "rb"))
                    os.remove(result)
                else:
                    await msg.reply('Command "PUZZLE": Wrong parameters')
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
