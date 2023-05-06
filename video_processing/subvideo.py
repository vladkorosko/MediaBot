import asyncio


async def subvideo(command, file_name):
    try:
        ffmpeg_command = f'ffmpeg -ss {int(command[2])} -i {file_name} -to {int(command[2])} -c:v copy -c:a copy {"result_" + file_name}'
        proc = await asyncio.create_subprocess_shell(
            ffmpeg_command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        _, stderr = await proc.communicate()
        if proc.returncode != 0:
            error_message = stderr.decode().strip()
            raise Exception(f'Error resizing video: {error_message}')
    except FileNotFoundError:
        return 'Missing file'

