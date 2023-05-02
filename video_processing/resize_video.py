import asyncio


async def resize_video(file_name: str, width: int, height: int):
    ffmpeg_cmd = """ffmpeg -i {0} -vf scale={1}:{2} {3}""".format(file_name, width, height,
                                                                  "result_" + file_name)
    proc = await asyncio.create_subprocess_shell(
        ffmpeg_cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    _, stderr = await proc.communicate()
    if proc.returncode != 0:
        error_message = stderr.decode().strip()
        raise Exception(f'Error resizing video: {error_message}')