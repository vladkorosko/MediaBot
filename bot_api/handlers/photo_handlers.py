import os

from aiogram import types

from photo_manager.crop_photo import crop_photo
from photo_manager.puzzle_photo import puzzle_photo
from photo_manager.resize_photo import resize_photo
from photo_manager.change_format_photo import convert_to_jpg, convert_to_jpeg, convert_to_png

from bot_api.handlers.cleaning_cache import send_and_delete


async def crop_photo_handler(input_file_name, input_file_format, msg, command, content_type):
    await msg.reply('Cropping')
    file_name = 'crop_' + input_file_name + '_' + str(msg.from_id) \
                + '_' + str(msg.message_id) + input_file_format
    if content_type == types.ContentType.PHOTO:
        await msg.photo[-1].download(file_name)
    elif content_type == types.ContentType.DOCUMENT:
        await msg.document.download(file_name)
    error = crop_photo(file_name, int(command[1]), int(command[2]), int(command[3]), int(command[4]))
    await send_and_delete(file_name, error, msg, input_file_format)


async def puzzle_photo_handler(input_file_name, input_file_format, msg, command, content_type):
    await msg.reply('Making puzzle')
    file_name = 'puzzle_' + input_file_name + '_' + str(msg.from_id) \
                + '_' + str(msg.message_id) + input_file_format
    if content_type == types.ContentType.PHOTO:
        await msg.photo[-1].download(file_name)
    elif content_type == types.ContentType.DOCUMENT:
        await msg.document.download(file_name)
    error = puzzle_photo(file_name, int(command[1]))
    await send_and_delete(file_name, error, msg, '.jpg')


async def resize_photo_handler(input_file_name, input_file_format, msg, command, content_type):
    await msg.reply('Resizing')
    file_name = 'resize_' + input_file_name + "_" + str(msg.from_id) + '_' \
                + str(msg.message_id) + input_file_format
    if content_type == types.ContentType.PHOTO:
        await msg.photo[-1].download(file_name)
    elif content_type == types.ContentType.DOCUMENT:
        await msg.document.download(file_name)
    error = resize_photo(file_name, int(command[1]), int(command[2]))
    await send_and_delete(file_name, error, msg, input_file_format)


async def change_format_photo_handler(input_file_name, input_file_format, msg, command, content_type):
    await msg.reply('Changing format')
    file_name = 'ch_format_' + input_file_name + "_" + str(msg.from_id) + '_' \
                + str(msg.message_id) + input_file_format
    if content_type == types.ContentType.PHOTO:
        await msg.photo[-1].download(file_name)
    elif content_type == types.ContentType.DOCUMENT:
        await msg.document.download(file_name)
    if command[1] in ['jpg', '.jpg']:
        error = convert_to_jpg(file_name)
        await send_and_delete(file_name, error, msg, '.jpg')
    elif command[1] in ['jpeg', '.jpeg']:
        error = convert_to_jpeg(file_name)
        await send_and_delete(file_name, error, msg, '.jpeg')
    elif command[1] in ['png', '.png']:
        error = convert_to_png(file_name)
        await send_and_delete(file_name, error, msg, '.png')
    else:
        os.remove(file_name)
        await msg.reply('Unsupported format: ' + command[1])
