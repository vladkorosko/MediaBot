import asyncio
from asgiref.sync import async_to_sync

from moviepy.editor import *
import os

from get_extension import get_format as gf


#@async_to_sync
async def convert_to_mp4(file_path):
    try:
        file_name, _ = gf(file_path)
        ffmpeg_command = f'ffmpeg -i {file_path} -c:v mpeg4 -preset fast -crf 19 {"result_" + file_name + ".mp4"}'

        process = await asyncio.create_subprocess_shell(
            ffmpeg_command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        _, stderr = await process.communicate()
        if process.returncode != 0:
            error_message = stderr.decode().strip()
            return f'Error resizing video: {error_message}'
    except FileNotFoundError:
        return 'Missing file'


def convert_avi_to_mp4_moviepy(avi_file_path, result_file_path):
    clip = VideoFileClip(avi_file_path)
    clip.write_videofile(result_file_path)


#@async_to_sync
async def convert_to_mov(file_path):
    try:
        file_name, file_format = gf(file_path)
        if file_format == '.avi':
            await convert_to_mp4(file_path)
            file_path = "result_" + file_name + ".mp4"
            # return "AVI files is not supported but you can first convert it mp4 and then to avi"
        ffmpeg_command = f'ffmpeg -i {file_path} -codec copy -movflags +faststart {"result_" + file_name + ".mov"}'
        process = await asyncio.create_subprocess_shell(
            ffmpeg_command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        _, stderr = await process.communicate()
        if file_format == '.avi':
            os.remove(file_path)
        if process.returncode != 0:
            error_message = stderr.decode().strip()
            return f'Error resizing video: {error_message}'
    except FileNotFoundError:
        return 'Missing file'

#@async_to_sync
async def convert_to_webm(file_path):
    try:
        file_name, file_format = gf(file_path)
        ffmpeg_command = f'ffmpeg -i {file_path} {"result_" + file_name + ".webm"}'
        if file_format == '.avi':
            await convert_to_mp4(file_path)
            file_path = "result_" + file_name + ".mp4"
            # return "AVI files is not supported but you can first convert it mp4 and then to avi"
        process = await asyncio.create_subprocess_shell(
            ffmpeg_command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        _, stderr = await process.communicate()
        if file_format == '.avi':
            os.remove(file_path)
        if process.returncode != 0:
            error_message = stderr.decode().strip()
            return f'Error resizing video: {error_message}'
    except FileNotFoundError:
        return 'Missing file'
