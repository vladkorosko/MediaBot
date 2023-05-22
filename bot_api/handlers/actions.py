from aiogram import types

from bot_api.dispatcher import dp
import bot_api.handlers.addion_functions as ad

from bot_api.handlers.photo_handlers import crop_photo_handler
from bot_api.handlers.photo_handlers import puzzle_photo_handler
from bot_api.handlers.photo_handlers import resize_photo_handler
from bot_api.handlers.photo_handlers import change_format_photo_handler

from bot_api.handlers.video_handlers import resize_video_handler
from bot_api.handlers.video_handlers import sub_video_handler
from bot_api.handlers.video_handlers import convert_video_handler

from get_extension import get_format as gf


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_crop = types.KeyboardButton('Crop')
    button_format = types.KeyboardButton('Format')
    button_puzzle = types.KeyboardButton('Puzzle')
    button_resize = types.KeyboardButton('Resize')
    button_subvideo = types.KeyboardButton('Subvideo')

    markup.add(button_crop, button_format, button_puzzle, button_resize, button_subvideo)

    await msg.reply('Bot for photo and video editing\n'
                    'Photo commands:\n - crop\n - format\n - puzzle\n - resize\n'
                    'Video commands: \n - format\n - resize\n - subvideo\n'
                    'For details send the name of command you want use.',
                    parse_mode="html", reply_markup=markup)


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handler_photo_message(msg):
    if msg.caption is not None:
        command = msg.caption.split()
        file_name = 'input'
        file_format = '.jpg'
        if command[0] == 'crop' and len(command) == 5:
            if ad.is_integer(command[1]) and ad.is_integer(command[2]) and ad.is_integer(command[3]) and ad.is_integer(
                    command[4]):
                await crop_photo_handler('input', '.jpg', msg, command, types.ContentType.PHOTO)
            else:
                await msg.reply('Command "CROP": Wrong parameters')
        elif command[0] == 'puzzle' and len(command) == 2:
            if ad.is_integer(command[1]):
                await puzzle_photo_handler('input', '.jpg', msg, command, types.ContentType.PHOTO)
            else:
                await msg.reply('Command "PUZZLE": Wrong parameters')
        elif command[0] == 'resize' and len(command) == 3:
            if ad.is_integer(command[1]) and ad.is_integer(command[2]):
                await resize_photo_handler('input', '.jpg', msg, command, types.ContentType.PHOTO)
            else:
                await msg.reply('Command "RESIZE": Wrong parameters')
        elif command[0] == 'format' and len(command) == 2:
            await change_format_photo_handler('input', '.jpg', msg, command, types.ContentType.PHOTO)
        else:
            await msg.reply('Photo: Wrong command')
    else:
        await msg.reply('Command is absent')


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def handle_file_message(msg):
    if msg.document is not None:
        if msg.caption is not None:
            file_name, file_format = gf(msg.document.file_name)
            command = msg.caption.split()
            if file_format in ['.bmp', '.jpg', '.jpeg', '.tiff', '.png']:
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
            elif file_format in ['.avi', '.mp4', '.mov', '.webm']:
                if command[0] == 'crop' and len(command) == 5:
                    if ad.is_integer(command[1]) and ad.is_integer(command[2]) and ad.is_integer(
                            command[3]) and ad.is_integer(
                            command[4]):
                        # await crop_video_handler('input', '.jpg', msg, command, types.ContentType.PHOTO)
                        pass
                    else:
                        await msg.reply('Command "CROP": Wrong parameters')
                elif command[0] == 'resize' and len(command) == 3:
                    if ad.is_integer(command[1]) and ad.is_integer(command[2]):
                        await resize_video_handler(file_name, file_format, msg, command,  types.ContentType.DOCUMENT)
                    else:
                        await msg.reply('Command "RESIZE": Wrong parameters')
                elif command[0] == 'subvideo' and len(command) == 3:
                    if ad.is_integer(command[1]) and ad.is_integer(command[2]):
                        await sub_video_handler(file_name, file_format, msg, command,  types.ContentType.DOCUMENT)
                    else:
                        await msg.reply('Command "SUBVIDEO": Wrong parameters')
                elif command[0] == 'format' and len(command) == 2:
                    await convert_video_handler(file_name, file_format, msg, command,  types.ContentType.DOCUMENT)
                else:
                    await msg.reply('Video: Wrong command')
            else:
                await msg.reply('Unsupported document format')
        else:
            await msg.reply('Command is absent')
    else:
        await msg.reply('Document is absent')


@dp.message_handler(content_types=types.ContentType.TEXT)
async def help_function(msg):
    if msg.text in ['puzzle', 'Puzzle']:
        await msg.reply('Send photo and in description write command \n<b><i>puzzle number</i></b> - '
                        'where:\n<b><i>number</i></b> - number of columns and rows. \nExample - "puzzle 4"',
                        parse_mode='html')
    elif msg.text in ['crop', 'Crop']:
        await msg.reply('Send photo or video and in description write command \n'
                        '<b><i>crop x_start y_start x_end y_end</i></b> - where:\n'
                        '<b><i>x_start y_start</i></b> - position of top right corner of photo in pixels;\n'
                        '<b><i>x_end y_end</i></b> - position of bottom left corner of photo in pixels. \n'
                        'Example - "crop 100 100 200 200"',
                        parse_mode='html')
    elif msg.text in ['format', 'Format']:
        await msg.reply('Send photo or video and in description write command \n<b><i>format result_format</i></b> - '
                        'where:\n<b><i>result_format</i></b> - '
                        'the format of the photo or video into which you want to convert.\n'
                        'Supported formats for photo:\n'
                        'from <b><i>BMP, GIF, JPEG, PNG or TIFF</i></b> to <b><i>JPEG(.jpeg, .jpg) or PNG</i></b>\n'
                        'Supported formats for video:\n'
                        'from <b><i>MOV, AVI, MP4, WEBM or WMV</i></b> to <b><i>MOV, WEBM or MP4</i></b>\n'
                        'Example - "format .jpg"',
                        parse_mode='html')
    elif msg.text in ['resize', 'Resize']:
        await msg.reply('Send photo or video and in description write command \n<b><i>resize width height</i></b> - '
                        'where:\n<b><i>width</i></b> - width of result photo or video in pixels;\n'
                        '<b><i>height</i></b> - height of result photo or video in pixels.\n'
                        'Example - "resize 512 512"',
                        parse_mode='html')
    elif msg.text in ['subvideo', 'Subvideo']:
        await msg.reply('Send video and in description write command \n'
                        '<b><i>subvideo start_second duration</i></b> - '
                        'where:\n<b><i>start_second</i></b> - start second of subvideo;\n'
                        '<b><i>duration</i></b> - duration of subvideo.\n'
                        'Example - "subvideo 5 10"',
                        parse_mode='html')
    else:
        await msg.reply('Unknown command: <b><i>{0}</i></b> - try again'.format(msg.text))


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def handle_video_message(msg):
    if msg.caption is not None:
        command = msg.caption.split()
        file_name, file_format = gf(msg.video.file_name)
        if command[0] == 'crop' and len(command) == 5:
            if ad.is_integer(command[1]) and ad.is_integer(command[2]) and ad.is_integer(command[3]) and ad.is_integer(
                    command[4]):
                #await crop_video_handler('input', '.jpg', msg, command, types.ContentType.PHOTO)
                pass
            else:
                await msg.reply('Command "CROP": Wrong parameters')
        elif command[0] == 'resize' and len(command) == 3:
            if ad.is_integer(command[1]) and ad.is_integer(command[2]):
                await resize_video_handler(file_name, file_format, msg, command, types.ContentType.VIDEO)
            else:
                await msg.reply('Command "RESIZE": Wrong parameters')
        elif command[0] == 'subvideo' and len(command) == 3:
            if ad.is_integer(command[1]) and ad.is_integer(command[2]):
                await sub_video_handler(file_name, file_format, msg, command, types.ContentType.VIDEO)
            else:
                await msg.reply('Command "SUBVIDEO": Wrong parameters')
        elif command[0] == 'format' and len(command) == 2:
            await convert_video_handler(file_name, file_format, msg, command, types.ContentType.VIDEO)
        else:
            await msg.reply('Video: Wrong command')
    else:
        await msg.reply('Command is absent')


@dp.message_handler(content_types=types.ContentType.ANIMATION)
async def handle_video_message(msg):
    await msg.reply("Animation")
