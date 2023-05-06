import asyncio


async def resize_video(file_name: str, width: int, height: int):
    try:
        ffmpeg_cmd = """ffmpeg -i {0} -vf scale={1}:{2} {3}""".format(file_name, width, height, "result_" + file_name)
        proc = await asyncio.create_subprocess_shell(
            ffmpeg_cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        _, stderr = await proc.communicate()
        if proc.returncode != 0:
            error_message = stderr.decode().strip()
            return f'Error resizing video: {error_message}'
    except FileNotFoundError:
        return 'Missing file'

