import asyncio

from aiogram import types

from video_processing.resize_video import resize_video_ffmpeg

from bot_api.dispatcher import bot

from bot_api.handlers.cleaning_cache import send_and_delete


async def resize_video_handler(input_file_name, input_file_format, msg, command, content_type):
    await msg.reply('Resizing')
    file_name = 'resize_' + input_file_name + "_" + str(msg.from_id) + '_' \
                + str(msg.message_id) + input_file_format
    if content_type == types.ContentType.VIDEO:
        file = await bot.get_file(msg.video.file_id)
        file_path = file.file_path
        await bot.download_file(file_path, file_name)
    elif content_type == types.ContentType.DOCUMENT:
        await msg.document.download(file_name)

    ffmpeg_cmd = """ffmpeg -i {0} -vf scale={1}:{2} {3}""".format(file_name, int(command[1]), int(command[2]), "result_" + file_name)
    proc = await asyncio.create_subprocess_shell(
        ffmpeg_cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    await proc.communicate()
    await send_and_delete(file_name, None, msg, input_file_format)
