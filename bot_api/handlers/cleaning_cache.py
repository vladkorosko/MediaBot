import os

from get_extension import get_format as gf


async def send_and_delete(input_file_name, error, msg, output_format):
    os.remove(input_file_name)
    file_name, file_format = gf(input_file_name)
    if error is None:
        result = 'result_' + file_name + output_format
        await msg.reply_document(open(result, "rb"))
        os.remove(result)
    else:
        await msg.reply(error)
