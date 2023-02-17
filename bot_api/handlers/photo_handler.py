import os

from aiogram import types

from photo_manager.crop_photo import crop_photo
from photo_manager.puzzle_photo import puzzle_photo
from photo_manager.resize_photo import resize_photo
from get_extension import get_format as gf


async def end_photo_operation(file_name, error, msg):
    os.remove(file_name)
    file_name, file_format = gf(file_name)
    if error is None:
        result = file_name + '_result' + file_format
        await msg.reply_document(open(result, "rb"))
        os.remove(result)
    else:
        await msg.reply(error)


async def crop_photo_handler(input_file_name, input_file_format, msg, command, content_type):
    await msg.reply("Cropping")
    file_name = "crop_" + input_file_name + "_" + str(msg.from_id) \
                + '_' + str(msg.message_id) + '.' + input_file_format
    if content_type == types.ContentType.PHOTO:
        await msg.photo[-1].download(file_name)
    elif content_type == types.ContentType.DOCUMENT:
        await msg.document.download(file_name)
    error = crop_photo(file_name, int(command[1]), int(command[2]), int(command[3]), int(command[4]))
    await end_photo_operation(file_name, error, msg)


async def puzzle_photo_handler(input_file_name, input_file_format, msg, command, content_type):
    await msg.reply("Making puzzle")
    file_name = "puzzle_" + input_file_name + "_" + str(msg.from_id) \
                + '_' + str(msg.message_id) + '.' + input_file_format
    if content_type == types.ContentType.PHOTO:
        await msg.photo[-1].download(file_name)
    elif content_type == types.ContentType.DOCUMENT:
        await msg.document.download(file_name)
    error = puzzle_photo(file_name, int(command[1]))
    await end_photo_operation(file_name, error, msg)


async def resize_photo_handler(input_file_name, input_file_format, msg, command, content_type):
    await msg.reply("Resizing")
    file_name = "input_" + input_file_name + "_" + str(msg.from_id) + '_' \
                + str(msg.message_id) + '.' + input_file_format
    if content_type == types.ContentType.PHOTO:
        await msg.photo[-1].download(file_name)
    elif content_type == types.ContentType.DOCUMENT:
        await msg.document.download(file_name)
    error = resize_photo(file_name, int(command[1]), int(command[2]))
    await end_photo_operation(file_name, error, msg)
