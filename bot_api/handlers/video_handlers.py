import os

import aiogram.utils.exceptions
from aiogram import types

from video_processing.resize_video import resize_video
from video_processing.subvideo import subvideo
from video_processing.format_conversion import convert_to_mp4, convert_to_webm, convert_to_mov

from bot_api.dispatcher import bot

from bot_api.handlers.cleaning_cache import send_and_delete


async def download_video(content_type, msg, file_name):
    try:
        if content_type == types.ContentType.VIDEO:
            file = await bot.get_file(msg.video.file_id)
            file_path = file.file_path
            await bot.download_file(file_path, file_name)
        elif content_type == types.ContentType.DOCUMENT:
            await msg.document.download(file_name)
    except aiogram.utils.exceptions.FileIsTooBig:
        raise Exception("File is too big")


async def resize_video_handler(input_file_name, input_file_format, msg, command, content_type):
    await msg.reply('Resizing')
    file_name = 'resize_' + input_file_name + "_" + str(msg.from_id) + '_' \
                + str(msg.message_id) + input_file_format
    try:
        await download_video(content_type, msg, file_name)

        errors = await resize_video(file_name, int(command[1]), int(command[2]))
        await send_and_delete(file_name, errors, msg, input_file_format)
    except:
        await msg.reply("File is too big")


async def sub_video_handler(input_file_name, input_file_format, msg, command, content_type):
    await msg.reply('Making video')
    file_name = 'subvideo_' + input_file_name + "_" + str(msg.from_id) + '_' \
                + str(msg.message_id) + input_file_format
    try:
        await download_video(content_type, msg, file_name)

        errors = await subvideo(command, file_name)
        await send_and_delete(file_name, errors, msg, input_file_format)
    except:
        await msg.reply("File is too big")


async def convert_video_handler(input_file_name, input_file_format, msg, command, content_type):
    await msg.reply('Changing format')
    file_name = 'format_' + input_file_name + "_" + str(msg.from_id) + '_' \
                + str(msg.message_id) + input_file_format
    try:
        await download_video(content_type, msg, file_name)

        if command[1] in ['mp4', '.mp4']:
            errors = await convert_to_mp4(file_name)
            await send_and_delete(file_name, errors, msg, '.mp4')
        elif command[1] in ['mov', '.mov']:
            errors = await convert_to_mov(file_name)
            await send_and_delete(file_name, errors, msg, '.mov')
        elif command[1] in ['webm', '.webm']:
            errors = await convert_to_webm(file_name)
            await send_and_delete(file_name, errors, msg, '.webm')
        else:
            os.remove(file_name)
            await msg.reply('Unsupported format: ' + command[1])
    except:
        await msg.reply("File is too big")
